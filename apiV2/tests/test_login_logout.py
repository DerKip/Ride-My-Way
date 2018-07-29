from ..tests.base_test import BaseTestCase
from ..models.models import db, initialize, drop
import json
class LoginTestCase(BaseTestCase):
    """This class represents login test case""" 

    def setUp(self):
        super().setUp()
        db.__init__()
        drop()
        initialize()
        self.data = {
            "user":{
                    "username":"Derrick",
                    "email":"dkip64@gmail.com",
                    "contact":"0721611441",
                    "password":"TakeMethere1!",
                    "confirm_password":"TakeMethere1!"
                    },
            "login":{
                    "username":"Derrick",
                    "password":"TakeMethere1!"  
                    },
       "wrong_pass":{
                    "username":"Derrick",
                    "password":"gg"
                    },
             "fake":{
                    "username":"desparado",
                    "password":"despa"
                    }, 
                } 
        
    def tearDown(self):
        drop()

    def test_user_can_login(self):
        """Test whether user can log in"""
        res = self.client().post(self.full_url('auth/signup'),data=json.dumps(self.data["user"]),
        content_type='application/json')
        res = self.client().post(self.full_url('auth/login'),data=json.dumps(self.data["login"]),
        content_type='application/json')
        self.assertEqual(res.status_code,200)

    def test_unknown_user_cannot_login(self):
        """Test whether unknown user cannot log in"""
        res = self.client().post(self.full_url('auth/login'),data=json.dumps(self.data["fake"]),
        content_type='application/json')
        self.assertEqual(res.status_code,400)
    
    def test_wrong_password(self):
        """Test whether a user cannot log in with a wrong password"""
        res = self.client().post(self.full_url('auth/signup'),data=json.dumps(self.data["user"]),
        content_type='application/json')
        res = self.client().post(self.full_url('auth/login'),data=json.dumps(self.data["wrong_pass"]),
        content_type='application/json')
        self.assertEqual(res.status_code,401)


    