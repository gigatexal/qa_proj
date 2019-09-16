from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
import os

from views.Auth import UserLoginView
from views.Project import ProjectView
from views.User import UserCreateView
from views.Test import TestView
from views.Test import TestRunnerView
from views.Test import TestResultsView

app = Flask(__name__)
api = Api(app)
app.config['JWT_SECRET_KEY']=os.environ['JWT_SECRET_KEY']
jwt = JWTManager(app)

api.add_resource(UserCreateView, '/api/v1/user')
api.add_resource(UserLoginView, '/api/v1/login')
api.add_resource(ProjectView, '/api/v1/project')
api.add_resource(TestView, '/api/v1/<project_name>/test')
api.add_resource(TestRunnerView, '/api/v1/<project_name>/<test_name>/run')
api.add_resource(TestResultsView, '/api/v1/<project_name>/<test_name>/<run_id>')

if __name__ == '__main__':
    app.run(debug=True)