from models.user import UserData

class DriverData(UserData):
    """This class stores drivers data"""

    def __init__(self, username,email,password,car_model,car_regno):
        super().__init__(username,email,password)
        self.username = username
        self.email = email
        self.password = password

    drivers = []
