from flask_jwt_extended import get_jwt_claims, jwt_required

from models.project import Project
from views.Base import BaseView
from models.Requests.CreateTestRequest import CreateTestRequest

class TestView(Project, BaseView):
    def __init__(self):
        super(TestView, self).__init__()
    
    @jwt_required
    def post(self, project_name):
        args = CreateTestRequest.parse_args()
        test_name = args['name']
        claims = get_jwt_claims()
        if claims['create_test']=='True':
            project_id = self.get_by_name(project_name)
            id_ = self.create_test(name=test_name, project_id=project_id)
            return {'msg': f"test created, test id: {id_}"}, 201
        else:
            return {'error': "unable to create test for project {project_name}"}, 400

class TestRunnerView(Project, BaseView):
    def __init__(self):
        super(TestRunnerView, self).__init__()
    
    @jwt_required
    def post(self, project_name, test_name):
        claims = get_jwt_claims()
        if claims['run_test']=='True':
           project_id = self.get_by_name(name=project_name)
           test_id = self.get_test_by_name(project_id=project_id, test_name=test_name)
           self.run_test(test_id=test_id)
           return {'test_run_id': test_id}

class TestResultsView(Project, BaseView):
    def __init__(self):
        super(TestResultsView, self).__init__()
    
    @jwt_required
    def get(self, project_name, test_name, run_id):
        claims = get_jwt_claims()
        if claims['view_test_results']=='True':
            result = self.get_test_run_result(test_run_id=run_id)
            return {'test_results': f"project: {project_name} test_name: {test_name} result: {result}"}
        else:
            return {'error': "unable to get test results"}