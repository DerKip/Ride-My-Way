from tests.base_test import BaseTestCase
import json
class RegistrationTestCase(BaseTestCase):
    """ This class represents resgistration test case """

    def setUp(self):
        super().setUp()
        self.user = {
            "username":"Derrick",
            "email":"derrick97kirwa@gmail.com",
            "password":"#derkIp",
            "confirm_password":"#derkIp"
        }
        self.driver = {
            "username":"Angela",
            "email":"Angelina@gmail.com",
            "car_model":"Mark x",
            "car_regno":"KCR 127F",
            "password":"angelina",
            "confirm_password":"angelina"     
        }
    
    def test_user_can_register(self):
        """test whether user can register"""
        res=self.client().post(self.full_url('user/register'), data=json.dumps(dict(self.user)),
        content_type='application/json')
        self.assertEqual(res.status_code,201) #created

    def test_one_can_register_as_driver(self):
        """test whether user a user can register as a driver"""
        res=self.client().post(self.full_url('driver/register'), data=json.dumps(dict(self.driver)),
        content_type='application/json')
        self.assertEqual(res.status_code,201) #created
