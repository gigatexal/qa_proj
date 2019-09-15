from db.conn import transaction

class User(object):
    def create(self, email, phash, role): # return id of newly created user
        with transaction() as txn_conn:
            with txn_conn.cursor() as cursor:
                role_stmt = '''SELECT id FROM "roles" WHERE name = %s'''
                cursor.execute(role_stmt, [role])
                role_id = cursor.fetchone()
                create_user_stmt = '''INSERT INTO "users" (email, phash, role_id) SELECT %s, %s, %d'''
                cursor.execute(create_user_stmt, [email, phash, role_id])
                id_ = cursor.fetchone()
                return id_
    
    def exists(self, email, phash): # returns id
        with transaction() as txn_conn:
            with txn_conn.cursor() as cursor:
                user_existence_check = '''SELECT id FROM "users" WHERE email = %s and phash = %s'''
                cursor.execute(user_existence_check, [email, phash])
                id_ = cursor.fetchone()
                return id_
    
    def get_user_roles(self, uid):
        with transaction() as txn_conn:
            with txn_conn.cursor() as cursor:
                fetch_user_abilities = 
                    '''
                        SELECT r.abilities
                        FROM "roles" r
                        INNER JOIN "users" u
                            ON u.role_id = r.id
                    '''
                cursor.execute(fetch_user_abilities, [uid])
                abilities = cursor.fetchone()
                return abilities
    


    def delete(self):
        # TODO: implement
        pass