from models.user import UserData

drivers = []

class DriverData(UserData):
    """This class stores drivers data"""

    def __init__(self, username,email,password,car_model,car_regno):
        super().__init__(username,email,password)
        self.car_model = car_model
        self.car_regno = car_regno

    
