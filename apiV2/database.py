import psycopg2
from psycopg2.extras import RealDictCursor

class Database():
    """ This class contains the db connection method"""
    conn = None 
    cursor = None    
    app = None

    def init_app(self, app):
        self.app = app
        self.conn = psycopg2.connect(
                                    database=app.config['DATABASE_NAME'],
                                    user=app.config['DATABASE_USER'],
                                    password=app.config['DATABASE_USER'],
                                    host=app.config['DATABASE_HOST'],
                                    )
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)