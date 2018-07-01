import psycopg2
from .database import Database
from psycopg2.extras import RealDictCursor
from apiV2 import app
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

db = Database(app)

class User():
    def __init__(self, username, email, password, car_model, car_regno, contact):
        self.username = username
        self.email = email
        self.password = password
        self.car_model = car_model
        self.car_regno = car_regno
        self.contact = contact

    def create_user(self):
        db.cur.execute("""INSERT INTO users( username, email, password, car_model, car_regno, contact)
                             VALUES(%s,%s,%s,%s,%s,%s)""",
                                (
                                    self.username, 
                                    self.email,
                                    self.password,
                                    self.car_model,
                                    self.car_regno,
                                    self.contact,
                                )
                          )
        db.conn.commit()

def drop():
    db.query("""DROP TABLE IF EXISTS user""")
    db.query("""DROP TABLE IF EXISTS rides""")
    db.query("""DROP TABLE IF EXISTS requests""")
    db.conn.commit()

def initialize():
    db.query("""CREATE TABLE users(
            id serial PRIMARY KEY,
            username VARCHAR(255),
            email VARCHAR(255),
            password VARCHAR(255),        
            car_model VARCHAR(255),
            car_regno VARCHAR(255)
            )
            """)
    db.query("""CREATE TABLE rides(
            id serial PRIMARY KEY,
            created_by VARCHAR(255),
            destination VARCHAR(255),
            from_location VARCHAR(255),
            price VARCHAR DEFAULT 'FREE',
            departure_time VARCHAR(255),
            date_created TIMESTAMP DEFAULT NOW()
        )
            """)
    db.query("""CREATE TABLE requests(
            id serial PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            ride_id INTEGER REFERENCES rides(id),
            response CHAR DEFAULT 'no responses'
        )
            """)

    db.conn.commit()

def get_users():
    db.cur.execute("SELECT id, username, email, car_model, car_regno FROM users")
    db.conn.commit()
    users = db.cur.fetchall()
    return users

def get_user(user):
    db.cur.execute("SELECT * FROM users WHERE username = (%s)",(user,))
    db.conn.commit() 
    user = db.cur.fetchone()
    return user

def get_user_by_id(userid):
    db.cur.execute("SELECT * FROM users WHERE id = (%s)",(userid,))
    db.conn.commit() 
    user_id = db.cur.fetchone()
    return user_id

def get_username(userid):
    user_dict= dict(get_user_by_id(userid))
    return user_dict["username"]

class Rides():
    def __init__(self, created_by, destination, from_location, price ,departure_time, date_created =''):
        self.created_by = created_by
        self.destination = destination
        self.from_location = from_location
        self.price = price
        self.departure_time = departure_time
        self.date_created = datetime.datetime.now()

    def create_ride(self):
        db.cur.execute("""INSERT INTO rides (created_by, destination, from_location, price, departure_time)
                             VALUES(%s,%s,%s,%s,%s)""",
                            (
                                self.created_by,
                                self.destination,
                                self.from_location,
                                self.price,
                                self.departure_time,
        
                            )
                        )
        db.conn.commit()
    
def get_all_rides():
    db.cur.execute("SELECT * FROM rides")
    db.conn.commit()
    rides = db.cur.fetchall()
    return rides


def get_ride_by_id(rideid):
    db.cur.execute("SELECT * FROM rides WHERE id = (%s)",(rideid,))
    db.conn.commit()
    ride_id = db.cur.fetchone()
    return ride_id

def get_driver_rides(created_by):
    db.cur.execute(
        "SELECT * FROM rides WHERE created_by = (%s)", (created_by))
    db.conn.commit()
    driver_rides = db.cur.fetchall()
    return driver_rides

class Requests():
    def __init__(self,user_id,ride_id,response):
        self.user_id = user_id
        self.ride_id = ride_id
        self.response = response

    def create_request(self):
        db.cur.execute("""INSERT INTO requests (user_id, ride_id, response)
                             VALUES(%s,%s,%s)""",
                            (
                                self.user_id,
                                self.ride_id,
                                self.response
                            )
                        )
        db.conn.commit()

def get_request_id(requestid):
    db.cur.execute("SELECT * FROM requests WHERE id = (%s)",(requestid,))
    db.conn.commit()
    request_id= db.cur.fetchone()
    return request_id

def get_all_requests(rideid):
    db.cur.execute("""  SELECT username, contact, ride_id FROM users
                        INNER JOIN requests on users.id = requests.user_id
                        WHERE requests.ride_id = (%s)""",(rideid,))
    db.conn.commit()
    requests = db.cur.fetchall()
    return requests
