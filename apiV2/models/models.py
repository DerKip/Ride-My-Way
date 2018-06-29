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
            price INTEGER,
            departure_time VARCHAR(255),
            date_created VARCHAR(255)
        )
            """)
    db.query("""CREATE TABLE requests(
            id serial PRIMARY KEY,
            ride_id INTEGER,
            username VARCHAR(255),
            email VARCHAR(255),
            contact VARCHAR(255),
            status VARCHAR(255)
        )
            """)

    db.conn.commit()

def get_users():
    db.cur.execute("SELECT * FROM users")
    db.conn.commit()
    users = db.cur.fetchall()
    return users

def get_user(user):
    db.cur.execute("SELECT * FROM users WHERE username = (%s)",(user,))
    db.conn.commit()
    user = db.cur.fetchone()
    return user

class Rides():
    def __init__(self, created_by, destination, from_location, price, departure_time):
        self.created_by = created_by
        self.destination = destination
        self.from_location = from_location
        self.price = price
        self.departure_time = departure_time
        self.date_created = str(datetime.datetime.now())[:10]

    def create_ride(self):
        db.cur.execute("""INSERT INTO rides (created_by, destination, from_location, price, departure_time)
                             VALUES(%s,%s,%s,%s,%s)""",
                            (
                                self.created_by,
                                self.destination,
                                self.from_location,
                                self.price,
                                self.departure_time
                            )
                        )
        db.conn.commit()
    
def get_all_rides(self):
    db.cur.execute("SELECT * FROM rides")
    db.conn.commit()
    rides = db.cur.fetchall()
    return rides


def get_ride_by_id(self,ride_id):
    db.cur.execute("SELECT * FROM rides WHERE id = (%s)",(ride_id))
    db.conn.commit()
    ride_id = db.cur.fetchone()
    return ride_id

def get_driver_rides(created_by):
    db.cur.execute(
        "SELECT * FROM rides WHERE created_by = (%s)", (created_by))
    db.conn.commit()
    driver_rides = db.cur.fetchall()
    return driver_rides