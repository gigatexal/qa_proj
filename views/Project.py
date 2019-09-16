from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_claims

from models.Requests.CreateProjectRequest import ProjectRequest
from models.project import Project

class ProjectView(Resource, Project):
    def __init__(self):
        super(ProjectView, self).__init__()

    @jwt_required
    def post(self):
        args = ProjectRequest.parse_args()
        name = args['name']
        claims = get_jwt_claims()
        if claims['create_project']=='True':
            self.create(name=name)
            return {'msg': f"project '{name}' created"}, 201
        else:
            return {'error':'insufficient permissions'}, 403
        