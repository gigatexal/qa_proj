from flask_restful import reqparse

CreateRequest = reqparse.RequestParser()
CreateRequest.add_argument('email', required=True, nullable=False)
CreateRequest.add_argument('phash', required=True, nullable=False)
CreateRequest.add_argument('role', required=True, nullable=False, choices=('admin', 'manager', 'qa_manager', 'user'))
