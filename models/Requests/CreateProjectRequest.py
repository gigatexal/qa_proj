from flask_restful import reqparse

ProjectRequest = reqparse.RequestParser()
ProjectRequest.add_argument('name', required=True, nullable=False)

