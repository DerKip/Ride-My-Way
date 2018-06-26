from ..tests.base_test import BaseTestCase
import json
class LoginTestCase(BaseTestCase):
    """This class represents login test case""" 

    def setUp(self):
        super().setUp()
        self.driver = {
            "username":"JeremyJohnson",
            "password":"password",
            "email":"JJ@andela.com",
            "car_model":"Skoda",
            "car_regno":"KCA 15TY"
        }
        self.user = {
            "username":"Errick",
            "email":"dkip64@gmail.com",
            "password":"dkip"
        }
    def test_driver_can_login(self):
        """Test whether driver can log in"""
        res = self.client().post(self.full_url('driver/register'),data=json.dumps(dict(self.driver)),
        content_type='application/json')
        self.assertEqual(res.status_code,201)

        res = self.client().post(self.full_url('login'),data=json.dumps(dict(self.driver)),
        content_type='application/json')
        self.assertEqual(res.status_code,200)
    
    def test_user_can_login(self):
        """Test whether user can log in"""
        res = self.client().post(self.full_url('user/register'),data=json.dumps(dict(self.user)),
        content_type='application/json')
        self.assertEqual(res.status_code,201)

        res = self.client().post(self.full_url('login'),data=json.dumps(dict(self.user)),
        content_type='application/json')
        self.assertEqual(res.status_code,200)

    def test_driver_can_logout(self):
        """Test whether driver logout"""
        res = self.client().delete(self.full_url('driver/logout'))
        self.assertEqual(res.status_code,200) #logout

    def test_user_can_logout(self):
        """Test whether user can logout"""
        res = self.client().delete(self.full_url('user/logout'))
        self.assertEqual(res.status_code,200) #logout
    