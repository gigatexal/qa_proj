from flask_restful import reqparse

CreateTestRequest = reqparse.RequestParser()
CreateTestRequest.add_argument('name', required=True, nullable=False)

