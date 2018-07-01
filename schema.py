import psycopg2
import sys
from apiV2 import app
from apiV2.models.database import Database
 

db = Database(app)

def main():
    try:
        db.query("""DROP TABLE IF EXISTS users CASCADE """)
        db.query("""DROP TABLE IF EXISTS rides CASCADE""")
        db.query("""DROP TABLE IF EXISTS requests CASCADE""")
       
        db.query("""CREATE TABLE users(
            id serial PRIMARY KEY,
            username VARCHAR(255),
            email VARCHAR(255),
            password VARCHAR(255),        
            car_model VARCHAR(255),
            car_regno VARCHAR(255),
            contact VARCHAR(255)
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
            response VARCHAR(255) DEFAULT 'no_response',
            status VARCHAR(255) DEFAULT 'pending'
        )
            """)

        db.conn.commit()
        db.conn.close()

    except psycopg2.Error:
        raise SystemExit("Failed {}".format(sys.exc_info()))
 


if __name__ == "__main__":
    main()

print ("--------- CREATED TABLES ---------")