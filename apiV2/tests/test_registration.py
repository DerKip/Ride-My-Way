from ..tests.base_test import BaseTestCase
from ..models.models import db, initialize, drop
import json
class RegistrationTestCase(BaseTestCase):
    """ This class represents resgistration test case """

    def setUp(self):
        super().setUp()
        db.__init__()
        drop()
        initialize()
        self.data = {
            "user":{
                    "username":"Errick",
                    "email":"dkip64@gmail.com",
                    "contact":"0721611441",
                    "password":"TakeMethere1!",
                    "confirm_password":"TakeMethere1!"
                    },
            "user1":{
                    "username":"Emannuel",
                    "email":"dkip64@gmail.com",
                    "contact":"0778161441",
                    "password":"Van#dgert3",
                    "confirm_password":"Van#dgert3"
                    },
            "spaces":{
                    "username":"  ",
                    "email":"dkip64@gmail.com",
                    "contact":"   ",
                    "password":"TakeMethere1!",
                    "confirm_password":"TakeMethere1!"
                    },
            "user2":{
                    "username":"",
                    "email":"",
                    "password":"#derkIp",
                    "confirm_password":"#derkIp"
                    },
          "mismatch":{
                    "username":"Jon",
                    "email":"Doe",
                    "password":"#derkIp",
                    "confirm_password":"#dkIp"
                    },
            "weak":{
                    "username":"Jon",
                    "email":"Doe",
                    "password":"jon",
                    "confirm_password":"jon"
                    },
    "invalid_email":{
                    "username":"Angelina",
                    "email":"Angelinagmail.scom",
                    "password":"angelina",
                    "confirm_password":"angelina"     
                    }
        }
    

    def tearDown(self):
        drop()

    def test_user_can_register(self):
        """test whether user can register"""
        res=self.client().post(self.full_url('auth/signup'), data=json.dumps(self.data["user"]),
        content_type='application/json')
        self.assertEqual(res.status_code,201)

    def test_user_cannot_register_twice(self):
        """test whether user cannot  register twice"""
        res=self.client().post(self.full_url('auth/signup'), data=json.dumps(self.data["user"]),
        content_type='application/json')
        res=self.client().post(self.full_url('auth/signup'), data=json.dumps(self.data["user"]),
        content_type='application/json') #checks if user can't register with existing user details
        self.assertEqual(res.status_code,409)

    def test_user_cannot_register_with_empty_spaces(self):
        """test whether user a user cannot register with empty spaces in fields"""
        res=self.client().post(self.full_url('auth/signup'), data=json.dumps(self.data["spaces"]),
        content_type='application/json')
        self.assertEqual(res.status_code,400)

    def test_user_cannot_register_with_missing_fields(self):
        """test whether user a user cannot register with missing fields"""
        res=self.client().post(self.full_url('auth/signup'), data=json.dumps(self.data["user2"]),
        content_type='application/json')
        self.assertEqual(res.status_code,400) #bad request
    
    def test_weak_password(self):
        """test whether a user cannot register with a weak password"""
        res=self.client().post(self.full_url('auth/signup'), data=json.dumps(self.data["weak"]),
        content_type='application/json')
        self.assertEqual(res.status_code,400)
    
    def test_email(self):
        """test whether a user email is valid"""
        res=self.client().post(self.full_url('auth/signup'), data=json.dumps(self.data["invalid_email"]),
        content_type='application/json')
        self.assertEqual(res.status_code,400) 
    
    def test_password_mismatch(self):
        """test whether confirm password matches with given password """
        res=self.client().post(self.full_url('auth/signup'), data=json.dumps(self.data["mismatch"]),
        content_type='application/json')
        self.assertEqual(res.status_code,400) 
    
    def test_user_can_register_without_filling_car_details(self):
        """test whether user a user can register without filling car details which isn't neccessary"""
        res=self.client().post(self.full_url('auth/signup'), data=json.dumps(self.data["user"]),
        content_type='application/json')
        self.assertEqual(res.status_code,201) 
    
    def test_user_cannot_register_with_existing_email(self):
        """test whether user a user cannot register with email already in use"""
        res=self.client().post(self.full_url('auth/signup'), data=json.dumps(self.data["user"]),
        content_type='application/json')
        res=self.client().post(self.full_url('auth/signup'), data=json.dumps(self.data["user1"]),
        content_type='application/json')
        self.assertEqual(res.status_code,409)
    
    def test_user_cannot_register_with_existing_username(self):
        """test whether user a user cannot register with username already in use"""
        res=self.client().post(self.full_url('auth/signup'), data=json.dumps(self.data["user"]),
        content_type='application/json')
        res=self.client().post(self.full_url('auth/signup'), data=json.dumps(self.data["user"]),
        content_type='application/json')
        self.assertEqual(res.status_code,409)

  