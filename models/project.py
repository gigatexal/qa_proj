import random

from db.conn import transaction


TEST_RESULT_VALUES = {
    "pass":      "SUCCEEDED",
    "fail":      "FAILED",
    "cancel":    "ABORTED"
}

# TODO: refactor with try/except and re-raise

class Project(object):
    def create(self, name): # returns the project id
        with transaction() as txn_conn:
            with txn_conn.cursor() as cursor:
                stmt = '''INSERT INTO "projects" (name) SELECT %s RETURNING id;'''
                cursor.execute(stmt, [name])
                id_, = cursor.fetchone()
                return id_             

    def create_test(self, name, project_id): # returns the test id
        with transaction() as txn_conn:
            with txn_conn.cursor() as cursor:
                stmt = '''INSERT INTO "tests" (name, project_id) SELECT %s, %s::INTEGER RETURNING id;'''
                cursor.execute(stmt, [name, project_id])
                test_id, = cursor.fetchone()
                return test_id

    def run_test(self, test_id):
        with transaction() as txn_conn:
            with txn_conn.cursor() as cursor:
                stmt = '''INSERT INTO "test_results" (test_id) SELECT %s::INTEGER returning id;'''
                cursor.execute(stmt, [test_id])
                id_, = cursor.fetchone()
                self.set_test_result(test_id=id)
                return id_

    def set_test_result(self, test_id, result=None):
        if result is None or result not in TEST_RESULT_VALUES.keys():
            result = TEST_RESULT_VALUES[random.choice(list(TEST_RESULT_VALUES.keys()))]
        with transaction() as txn_conn:
            with txn_conn.cursor() as cursor:
                stmt = '''UPDATE "tests_results" SET result = %s WHERE test_id = %s::INTEGER'''
                cursor.execute(stmt, [result, test_id])
                return True
        return False

    def get_test_run_result(self, test_run_id):
        with transaction() as txn_conn:
            with txn_conn.cursor() as cursor:
                stmt = '''SELECT result from "tests_results" WHERE id = %s::INTEGER'''
                cursor.execute(stmt, [test_run_id])
                result, = cursor.fetchone()
                return result

    def delete(self, project_id):
        with transaction() as txn_conn:
            with txn_conn.cursor() as cursor:
                stmt = '''DELETE FROM "projects" WHERE id = %s::INTEGER'''
                cursor.execute(stmt, [project_id])
                return True
        return False

    def delete_test(self, test_id):
        with transaction() as txn_conn:
            with txn_conn.cursor() as cursor:
                stmt = '''DELETE FROM "tests" WHERE id = %s::INTEGER'''
                cursor.execute(stmt, [test_id])
                return True
        return False

    def get_by_name(self, name):
        with transaction() as txn_conn:
            with txn_conn.cursor() as cursor:
                stmt = '''SELECT id FROM "projects" WHERE name = %s'''
                cursor.execute(stmt, [name])
                id_, = cursor.fetchone()
                return id_

    def get_test_by_name(self, project_id, test_name): # return test.id
        with transaction() as txn_conn:
            with txn_conn.cursor() as cursor:
                stmt = '''
                    SELECT t.id
                    FROM "tests" t
                    INNER JOIN "projects" p
                        ON t.project_id = p.id
                    WHERE t.name = %s
                    AND t.project_id = %s::INTEGER'''
                cursor.execute(stmt, [test_name, project_id])
                id_, = cursor.fetchone()
                return id_

    

        
