from ..tests.base_test import BaseTestCase
from ..models.models import db, initialize, drop
import json

class UserTestCase(BaseTestCase):
    """This class represents User requests test case"""

    def setUp(self):
        """Defining the test variable and initializing the app"""
        super().setUp()
        db.__init__()
        drop()
        initialize()
        self.data = {
            "user":{
                    "username":"Emannuel",
                    "email":"dkip64@gmail.com",
                    "contact":"0721611441",
                    "car_model": "Mazzerati",
                    "car_regno": "KCJ 908Y",
                    "password":"Van#dgert3",
                    "confirm_password":"Van#dgert3"
                    },
            "login":{
                    "username":"Emannuel",
                    "password":"Van#dgert3",
                    },
            "login2":{
                    "username":"Angelina",
                    "password":"angelinA#22",
                    },
             "ride":{
                    "destination":"Westlands",
                    "from_location":"CBD",
                    "departure_time":"10:30",
                    "price":"300"
                    },
            "ride2":{
                    "destination":"Kilimani",
                    "from_location":"CBD",
                    "departure_time":"10:30",
                    "price":"300"
                    },
            "user2":{
                    "username":"Angelina",
                    "email":"Angelina@gmail.com",
                    "contact":"0722611441",
                    "password":"angelinA#22",
                    "confirm_password":"angelinA#22"     
                    },
         "response":{
                    "Response":"Accept"
                    }   
        }
        # user 1 signup and login to get tocken header
        self.client().post(self.full_url('auth/signup'),data=json.dumps(self.data["user"]),
        content_type='application/json')
        self.response = self.client().post(self.full_url('auth/login'),data=json.dumps(self.data["login"]),
        content_type='application/json')
        self.access_token = json.loads(self.response.data.decode())['token']
        self.auth_header = {'Authorization': 'Bearer {}'.format(self.access_token)}

        # user 2 signup and login to get tocken header
        self.client().post(self.full_url('auth/signup'),data=json.dumps(self.data["user2"]),
        content_type='application/json')
        self.response2 = self.client().post(self.full_url('auth/login'),data=json.dumps(self.data["login2"]),
        content_type='application/json')
        self.access_token2 = json.loads(self.response2.data.decode())['token']
        self.auth_header2 = {'Authorization': 'Bearer {}'.format(self.access_token2)}

    
    def test_invalid_content_type(self):
        """Test user can't POST invalid content type"""
        res = self.client().post(self.full_url('users/rides'), data=json.dumps(self.data["ride"]), headers=self.auth_header,
        content_type='text')
        self.assertEqual(res.status_code, 400)
        
    def test_user_can_create_ride_offer(self):
        """Test driver can create a ride offer (POST request)"""
        res = self.client().post(self.full_url('users/rides'), data=json.dumps(self.data["ride"]), headers=self.auth_header,
        content_type='application/json')
        self.assertEqual(res.status_code, 201)
    
    def test_user_can_update_ride_offer(self):
        """Test whether a driver can update a ride offer (PUT request)"""
        res = self.client().post(self.full_url('users/rides'), data=json.dumps(self.data["ride"]), headers=self.auth_header,
        content_type='application/json')
        res = self.client().put(self.full_url('users/rides/1/update'), data=json.dumps(self.data["ride2"]), headers=self.auth_header,
        content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_delete_ride_offer(self):
        """Test whether a driver can delete a ride offer (DELETE request)"""
        res = self.client().post(self.full_url('users/rides'), data=json.dumps(self.data["ride"]), headers=self.auth_header,
        content_type='application/json')
        res = self.client().delete(self.full_url('users/rides/1/delete'), headers=self.auth_header,
        content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_delete_ride_offer_without_privilleges(self):
        """Test whether a driver can delete a ride offer that he/she did not create(DELETE request)"""
        res = self.client().post(self.full_url('users/rides'), data=json.dumps(self.data["ride"]), headers=self.auth_header,
        content_type='application/json')
        res = self.client().delete(self.full_url('users/rides/1/delete'), headers=self.auth_header2,
        content_type='application/json')
        self.assertEqual(res.status_code, 405) 

    def test_create_ride_without_car(self):
        """Test user can't create a ride offer without registering car details (POST request)"""
        res = self.client().post(self.full_url('users/rides'), data=json.dumps(self.data["ride"]), headers=self.auth_header2,
        content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_user_can_get_all_rides_offers(self):
        """Test user can get all ride offer (GET request)"""
        res = self.client().get(self.full_url('users/rides'), headers=self.auth_header,
        content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_user_can_get_a_single_ride_offer(self):
        """Test user can get a ride offer by id (GET request)"""
        res = self.client().post(self.full_url('users/rides'), data=json.dumps(self.data["ride"]), headers=self.auth_header,
        content_type='application/json')
        res = self.client().get(self.full_url('users/rides/1'), headers=self.auth_header,
        content_type='application/json')
        self.assertEqual(res.status_code, 200)
    
    def test_request_(self):
        """Test user can send a request to join a ride offer (POST request)"""
        res = self.client().post(self.full_url('users/rides'), data=json.dumps(self.data["ride"]), headers=self.auth_header,
        content_type='application/json')
        res = self.client().post(self.full_url('users/rides/1/request'), headers=self.auth_header2,
        content_type='application/json')
        self.assertEqual(res.status_code, 200)
    
    def test_request_by_owner(self):
        """Test user can't send a request to join his/her own ride offer (POST request)"""
        res = self.client().post(self.full_url('users/rides'), data=json.dumps(self.data["ride"]), headers=self.auth_header,
        content_type='application/json')
        res = self.client().post(self.full_url('users/rides/1/request'), headers=self.auth_header,
        content_type='application/json')
        self.assertEqual(res.status_code, 405)
    
    def test_request_by_rideid(self):
        """Test user can see requests sent a ride offer (GET request)"""
        res = self.client().post(self.full_url('users/rides'), data=json.dumps(self.data["ride"]), headers=self.auth_header,
        content_type='application/json')
        res = self.client().post(self.full_url('users/rides/1/request'), headers=self.auth_header2,
        content_type='application/json')
        res = self.client().get(self.full_url('users/rides/1/requests'),headers=self.auth_header,
        content_type='application/json')
        self.assertEqual(res.status_code,200)
    
    def test_request_by_rideid_with_no_request(self):
        """Test user can see a message if ride has no requests """
        res = self.client().post(self.full_url('users/rides'), data=json.dumps(self.data["ride"]), headers=self.auth_header,
        content_type='application/json')
        res = self.client().get(self.full_url('users/rides/1/requests'),headers=self.auth_header,
        content_type='application/json')
        self.assertEqual(res.status_code,404)
    
    def test_respond_to_request(self):
        """Test user can accept or reject request"""
        res = self.client().post(self.full_url('users/rides'), data=json.dumps(self.data["ride"]), headers=self.auth_header,
        content_type='application/json')
        res = self.client().post(self.full_url('users/rides/1/request'), headers=self.auth_header2,
        content_type='application/json')
        res = self.client().get(self.full_url('users/rides/1/requests/1'),data=json.dumps(self.data["response"]),headers=self.auth_header,
        content_type='application/json')
        self.assertEqual(res.status_code,200)
    
    def test_respond_to_non_existent_ride_id(self):
        """Test user can't accept or reject request for a non-existent rideid"""
        res = self.client().post(self.full_url('users/rides'), data=json.dumps(self.data["ride"]), headers=self.auth_header,
        content_type='application/json')
        res = self.client().get(self.full_url('users/rides/777/requests/1'),data=json.dumps(self.data["response"]),headers=self.auth_header,
        content_type='application/json')
        self.assertEqual(res.status_code,404)

    def test_user_cant_respond_without_privilleges(self):
        """Test user cant accept or reject request for ride he/she did not create"""
        res = self.client().post(self.full_url('users/rides'), data=json.dumps(self.data["ride"]), headers=self.auth_header,
        content_type='application/json')
        res = self.client().post(self.full_url('users/rides/1/request'), headers=self.auth_header2,
        content_type='application/json')
        res = self.client().get(self.full_url('users/rides/1/requests/1'),data=json.dumps(self.data["response"]),headers=self.auth_header2,
        content_type='application/json')
        self.assertEqual(res.status_code,405)
    
    

