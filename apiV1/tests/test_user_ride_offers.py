from ..tests.base_test import BaseTestCase
import json

class UserTestCase(BaseTestCase):
    """This class represents User requests test case"""

    def setUp(self):
        """Defining the test variable and initializing the app"""
        super().setUp()
        self.rideOffer={
                        "created_by":"Mark",
                        "destination":"Westlands",
                        "from_location":"Pumu",
                        "departure_time":"10:30",
                        "price":"300"
                        }
    
    def test_user_can_get_all_ride_offers(self):
        """Test user can get all ride offers (GET request)"""
        res = self.client().post(self.full_url('driver/create_ride'), data=json.dumps(dict(self.rideOffer)),
        content_type='application/json')
        self.assertEqual(res.status_code, 201) 

        res = self.client().get(self.full_url('user/rides'))
        self.assertEqual(res.status_code, 200) 

    def test_user_can_get_a_single_ride_offer(self):
        """Test user can get a ride offer by id (GET request)"""
        res = self.client().post(self.full_url('driver/create_ride'), data=json.dumps(dict(self.rideOffer)),
        content_type='application/json')
        self.assertEqual(res.status_code, 201)  #POST request on test ride offers

        res = self.client().get(self.full_url('user/rides/1'))
        self.assertEqual(res.status_code,200)

    def test_user_can_join_a_ride_offer(self):
        res = self.client().post(self.full_url('driver/create_ride'), data=json.dumps(dict(self.rideOffer)),
        content_type='application/json')
        self.assertEqual(res.status_code, 201)  #POST request on test ride offers

        res = self.client().post(self.full_url('user/rides/1/join'))
        self.assertEqual(res.status_code,200) #joined ride offer

    def test_user_can_see_joined_ride_offers(self):
        """Test whether users can see ride offers he/she has joined"""
        res = self.client().post(self.full_url('driver/create_ride'), data=json.dumps(dict(self.rideOffer)),
        content_type='application/json')
        self.assertEqual(res.status_code, 201) #POST ride offer

        res = self.client().post(self.full_url('user/rides/1/join'))
        self.assertEqual(res.status_code,200) #joined ride offer

        res = self.client().get(self.full_url('user/rides/joined'))
        self.assertEqual(res.status_code,200) 
          

    

