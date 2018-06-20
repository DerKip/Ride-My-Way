from tests.base_test import BaseTestCase

class LoginTestCase(BaseTestCase):
    """This class represents login test case""" 

    def setUp(self):
        super().setUp()
        self.driver = {
            "username":"JeremyJohnson",
            "password":"password"
        }
        self.user = {
            "username":"Derrick",
            "password":"dkip"
        }

    def test_driver_can_login(self):
        """Test whether driver can log in"""
        res = self.client().post(self.full_url('/login'), data=self.driver)
        self.assertEqual(res.status_code,200)
    
    def test_user_can_login(self):
        """Test whether user can log in"""
        res = self.client().post(self.full_url('/login'), data = self.user)
        self.assertEqual(res.status_code,200)

    def test_driver_can_logout(self):
        """Test whether driver can logout"""
        res = self.client().post(self.full_url('/login'), data = self.driver)
        self.assertEqual(res.status_code,200) #login first 

        res = self.client().delete(self.full_url('driver/logout'), data = self.driver)
        self.assertEqual(res.status_code,200) #logout

    def test_user_can_logout(self):
        """Test whether user can logout"""
        res = self.client().post(self.full_url('/login'), data = self.user)
        self.assertEqual(res.status_code,200) #login first 

        res = self.client().delete(self.full_url('user/logout'), data = self.user)
        self.assertEqual(res.status_code,200) #logout
    