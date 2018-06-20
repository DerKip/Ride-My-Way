from models.user import UserData

drivers = [{
                "id":1,
                "username":"Tabby",
                "email":"tabby@gmail.com",
                "car_model":"BMW",
                "car_regno":"KBG 009T",
                "password":"tabbytabbz",    
                },
                {
                "id":2,
                "username":"John",
                "email":"johnyy@gmail.com",
                "car_model":"BENZ",
                "car_regno":"KCG 909T",
                "password":"yulemse",    
                }]

class DriverData(UserData):
    """This class stores drivers data"""

    def __init__(self, username,email,password,car_model,car_regno):
        super().__init__(username,email,password)
        self.id = len (drivers)+ 1
        self.car_model = car_model
        self.car_regno = car_regno



    
