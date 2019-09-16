from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_claims

from models.user import User
from models.Requests.CreateUserRequest import CreateRequest

class UserCreateView(Resource, User):
    def __init__(self):
        super(UserCreateView, self).__init__()

    @jwt_required
    def post(self):
        args = CreateRequest.parse_args()
        email = args['email']
        phash = args['phash']
        role = args['role']
        try:
            claims = get_jwt_claims()
            if claims['can_create_users']=='True':
                self.create(email=email, phash=phash, role=role)
                return {'msg':'success'}, 201
        except Exception as e:
            print(e)
            return {'error': f'unable to create user'}, 500

    
