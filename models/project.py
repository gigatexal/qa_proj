import random

from db.conn import transaction


TEST_RESULT_VALUES = {
    "pass":      "SUCCEEDED",
    "fail":      "FAILED",
    "cancelled": "ABORTED"
}

class Project(object):
    def create(self, name): # returns the project id
        with transaction() as txn_conn:
            with txn_conn.cursor() as cursor:
                stmt = '''INSERT INTO "projects" (name) SELECT %s RETURNING id;'''
                cursor.execute(stmt, [name])
                id_ = cursor.fetchone()
                return id_             

    def create_test(self, name, project_id): # returns the test id
        with transaction() as txn_conn:
            with txn_conn.cursor() as cursor:
                stmt = '''INSERT INTO "tests" (name, project_id) SELECT %s, %d RETURNING id;'''
                cursor.execute(stmt, [name, project_id])
                id_ = cursor.fetchone()
                return id_

    def set_test_result(self, test_id, result=None):
        if result is None:
            result = TEST_RESULT_VALUES[random.choice(list(TEST_RESULT_VALUES.keys()))]
        pass

    def get_test_result(self, test_id):
        pass

    def delete(self, project_id=None):
        pass

    def delete_test(self, project_id=None, test_id=None):
        pass

    def get_by_id(self, id):
        pass

    def get_by_name(self, name):
        pass
    
