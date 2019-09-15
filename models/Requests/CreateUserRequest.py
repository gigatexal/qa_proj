from flask_restful import reqparse

ProjectRequest = reqparse.RequestParser()
ProjectRequest.add_argument('email', required=True, nullable=False)
ProjectRequest.add_argument('phash', required=True, nullable=False)
ProjectRequest.add_argument('role', required=True, nullable=False, choices=('admin', 'manager', 'qa_manager', 'user'))
