import os
from contextlib import contextmanager

import psycopg2

DB_URI = os.environ['DB_URI']

def connect(db_url=DB_URI):
    try:
        return psycopg2.connect(db_url)
    except Exception as e:
        # add logging
        print(e)

@contextmanager
def transaction(auto_commit=False, readonly=False, isolation_level=psycopg2.extensions.ISOLATION_LEVEL_DEFAULT):
    try:
        conn = connect()
        conn.set_session(isolation_level=isolation_level, readonly=readonly, autocommit=auto_commit)
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        # add logging
        raise e
    finally:
        conn.close()