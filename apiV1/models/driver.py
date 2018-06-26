from ..models.user import UserData

drivers = [{
                "car_model": "BMW",
                "car_regno": "KBG 009T",
                "email": "tabby@gmail.com",
                "id": 3,
                "password": "sha256$EKlzp9gg$e384a35d31484e4d2256a8ccac8a8d2327cf22a22ae7a4dd3e4efcdd21d454a0",
                "username": "Tabby"    
                },
                ]
class DriverData(UserData):
    """This class stores drivers data"""

    def __init__(self, username,email,password,car_model,car_regno):
        super().__init__(username,email,password)
        self.id = len (drivers)+ 1
        self.car_model = car_model
        self.car_regno = car_regno



    
