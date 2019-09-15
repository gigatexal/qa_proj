from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_claims, get_current_user

from models.Requests.CreateProjectRequest import ProjectRequest

class ProjectView(Resource):
    @jwt_required
    def post(self):
        args = ProjectRequest.parse_args()
        claims = get_jwt_claims()
        return args, 201
        