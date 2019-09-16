import datetime
import os

from flask_restful import Resource
from flask_jwt_extended import create_access_token, get_current_user

from models.user import User
from models.Requests.UserLoginRequest import LoginRequest

# TODO: Refresh token
# TODO: Logging

EXPIRY = datetime.timedelta(days=int(os.environ['JWT_EXPIRY']))

class UserLoginView(Resource, User):
    def __init__(self):
        super(UserLoginView, self).__init__()

    def post(self):
        args = LoginRequest.parse_args()
        email = args['email']
        phash = args['phash']
        claims = {}
        try:
            user_id = self.exists(email=email, phash=phash)
            user_claims = self.get_user_roles(user_id)
            claims.update(user_claims)
            access_token = create_access_token(identity={'user': email}, user_claims=claims, expires_delta=EXPIRY)
            return {'access_token': access_token}, 200
        except Exception as e:
            # TODO: What about a server error here, need to capture specific Exceptions...
            print(e)
            return {"error": f"unable to perform login"}, 401 