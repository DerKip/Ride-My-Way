from tests.base_test import BaseTestCase

class RegistrationTestCase(BaseTestCase):
    """ This class represents resgistration test case """

    def setUp(self):
        super().setUp()
        self.user = {
            "username":"Derrick",
            "email":"derrick97kirwa@gmail.com",
            "password":"#derkIp"
        }
        self.driver = {
            "username":"Tabby",
            "email":"tabby@gmail.com",
            "password":"tabbytabbz"
        }
    
    def test_user_can_register(self):
        """test whether user can register"""
        res=self.client().post(self.full_url('user/register'), data=self.user)
        self.assertEqual(res.status_code,201) #created

    def test_one_can_register_as_driver(self):
        """test whether user a user can register as a driver"""
        res=self.client().post(self.full_url('driver/register'), data=self.driver)
        self.assertEqual(res.status_code,201) #created
