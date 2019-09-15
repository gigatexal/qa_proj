from flask_restful import reqparse

LoginRequest = reqparse.RequestParser()
LoginRequest.add_argument('email', required=True, nullable=False, trim=True)
LoginRequest.add_argument('phash', required=True, nullable=False, trim=True)
