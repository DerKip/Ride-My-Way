from psycopg2 import connect
from psycopg2.extras import RealDictCursor

class Database(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.conn = connect("dbname='ride_my_way' user='postgres' host='localhost' password='admin'")
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def query(self, query):
        self.cur.execute(query)

    def close(self):
        self.cur.close()
        self.conn.close()