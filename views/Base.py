from flask_restful import Resource

class BaseView(Resource):
    def __init__(self):
        super(BaseView, self).__init__()

    def post(self):
       pass
    
    def get(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass