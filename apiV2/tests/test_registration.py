from ..tests.base_test import BaseTestCase
import json
class RegistrationTestCase(BaseTestCase):
    """ This class represents resgistration test case """

    def setUp(self):
        super().setUp()
        self.user = {
            "username":"DerricKip",
            "email":"derrick97kirwa@gmail.com",
            "password":"#derkIp",
            "confirm_password":"#derkIp"
        }
        self.user2 = {
            "username":"",
            "email":"",
            "password":"#derkIp",
            "confirm_password":"#derkIp"
        }
        self.driver = {
            "username":"Angelina",
            "email":"Angelina@gmail.com",
            "car_model":"Mark x",
            "car_regno":"KCR 127F",
            "password":"angelina",
            "confirm_password":"angelina"     
        }
    
        self.driver2 = {
            "username":"Angelina",
            "email":"",
            "car_model":"",
            "car_regno":"KCR 127F",
            "password":"angelina",
            "confirm_password":"angelina"     
        }
    
    def test_user_can_register(self):
        """test whether user can register"""
        res=self.client().post(self.full_url('user/register'), data=json.dumps(dict(self.user)),
        content_type='application/json')
        self.assertEqual(res.status_code,201) #created

    def test_user_cannot_register_twice(self):
        """test whether user cannot  register twice"""
        res=self.client().post(self.full_url('user/register'), data=json.dumps(dict(self.user)),
        content_type='application/json') #checks if user can't register with existing user details
        self.assertEqual(res.status_code,409)

    def test_user_cannot_register_with_missing_field(self):
        """test whether user a user cannot register with missing fields"""
        res=self.client().post(self.full_url('user/register'), data=json.dumps(dict(self.user2)),
        content_type='application/json')
        self.assertEqual(res.status_code,400) #bad request

    def test_driver_can_register_(self):
        """test whether driver can register"""
        res=self.client().post(self.full_url('driver/register'), data=json.dumps(dict(self.driver)),
        content_type='application/json')
        self.assertEqual(res.status_code,201) #created
        
    def test_driver_cannot_register_twice(self):
        """test whether driver cannot  register twice"""
        res=self.client().post(self.full_url('driver/register'), data=json.dumps(dict(self.driver)),
        content_type='application/json') #checks if user can't register with existing user details
        self.assertEqual(res.status_code,409)

    def test_driver_cannot_register_with_missing_field(self):
        """test whether driver cannot register with missing fields"""
        res=self.client().post(self.full_url('driver/register'), data=json.dumps(dict(self.driver2)),
        content_type='application/json')
        self.assertEqual(res.status_code,400) #bad request

    

    
    
