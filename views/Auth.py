import datetime
import os

from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, get_current_user

from models.Requests.UserLoginRequest import LoginRequest

# TODO: Refresh token
# TODO: Logging

ADMIN_DEFAULT_EMAIL = os.environ['ADMIN_DEFAULT_EMAIL'] 
ADMIN_DEFAULT_PHASH = os.environ['ADMIN_DEFAULT_PHASH']
USERS = {ADMIN_DEFAULT_EMAIL:ADMIN_DEFAULT_PHASH}

EXPIRY = datetime.timedelta(days=int(os.environ['JWT_EXPIRY']))

'''
@jwt.user_identity_loader
def user_identity_lookup(args):
    return args['email']
'''

class UserLoginView(Resource):
    def post(self):
        args = LoginRequest.parse_args()
        if args['email'] in USERS.keys():
            if args['phash'] == USERS[args['email']]:
                access_token = create_access_token(identity=args, user_claims={'can_create_tests':True}, expires_delta=EXPIRY)
                return {'access_token':access_token}, 200
        return {"error":"The user and/or password is incorrect. Please try again."}, 403
    