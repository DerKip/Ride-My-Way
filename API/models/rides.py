import datetime
all_ride_offers = []
class BaseRidesClass():
    """ This class represents the Base Ride Offers Class """

    def __init__(self, created_by, destination, from_location, price, departure_time):
        self.id = len(all_ride_offers)+1
        self.created_by = created_by
        self.destination = destination
        self.from_location = from_location #location which ride is from
        self.price = int(price) 
        self.departure_time = departure_time
        
        current_date = str(datetime.datetime.now())
        self.date_created = current_date[:10]



