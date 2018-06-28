import psycopg2
import sys
from apiV2 import app
from apiV2.models.database import Database
 

db = Database(app)

def main():
    try:
        db.query("""DROP TABLE IF EXISTS users""")
        db.query("""DROP TABLE IF EXISTS rides""")
        db.query("""DROP TABLE IF EXISTS requests""")
       
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
        db.conn.close()

    except psycopg2.Error:
        raise SystemExit("Failed {}".format(sys.exc_info()))
 


if __name__ == "__main__":
    main()

print ("--------- CREATED TABLES ---------")