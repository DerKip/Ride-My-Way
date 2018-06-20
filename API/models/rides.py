import datetime

all_ride_offers = []
joined_ride_offers = []
accepted_ride_offers = []

class BaseRidesClass():
    """ This class represents the Base Ride Offers Class """

    def __init__(self, driver, destination, from_location, price, departure_time):
        self.driver = driver
        self.destination = destination
        self.from_location = from_location #location which ride is from
        self.price = int(price) 
        self.departure_time = departure_time
        
        current_date = str(datetime.datetime.now())
        self.date_created = current_date[:10]

class JoinedRideOffers(BaseRidesClass):
    """ This class represents Ride Offers that have been joined """
    def __init__(self, driver, destination, from_location, price, departure_time,passenger):
        super().__init__(driver, destination, from_location, price, departure_time)
        self.passenger = passenger

class AcceptedRideOffers(JoinedRideOffers):
    """ This class represents Ride Offers that have been joined and accepted """
    def __init__(self, driver, destination, from_location, price, departure_time,passenger,accepted=False):
        super().__init__(driver, destination, from_location, price, departure_time, passenger)
        self.accepted = accepted



new_passenger=AcceptedRideOffers('Mark','Westi','Umo',30,'10:00','James')
print (new_passenger.__dict__)

