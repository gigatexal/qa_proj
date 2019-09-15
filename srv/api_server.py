from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
import os

from views.Auth import UserLoginView
from views.Project import ProjectView
from views.User import UserCreateView

app = Flask(__name__)
api = Api(app)
app.config['JWT_SECRET_KEY']=os.environ['JWT_SECRET_KEY']
jwt = JWTManager(app)

api.add_resource(UserCreateView, '/api/v1/user')
api.add_resource(UserLoginView, '/api/v1/login')
api.add_resource(ProjectView, '/api/v1/project')

if __name__ == '__main__':
    app.run(debug=True)