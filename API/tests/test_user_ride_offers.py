from tests.base_test import BaseTestCase

import datetime


class UserTestCase(BaseTestCase):
    """This class represents User requests test case"""

    def setUp(self):
        """Defining the test variable and initializing the app"""
        super().setUp()
        departuretime=str(datetime.datetime.now())[:16]
        self.rideOffer={
            "id":1,
            "destination":"Kileleshwa",
            "my_location":"Pangani",
            "depature_time":departuretime,
            }
    
    def test_user_can_get_all_ride_offers(self):
        """Test user can get all ride offers (GET request)"""
        res = self.client().post(self.full_url('users/ride_offers'), data=self.rideOffer)
        self.assertEqual(res.status_code, 201) #POST request on ride offers

        res = self.client().get(self.full_url('users/ride_offers'))
        self.assertEqual(res.status_code, 200)

    def test_user_can_get_a_single_ride_offer(self):
        """Test user can get a ride offer by id (GET request)"""
        res = self.client().post(self.full_url('users/ride_offers'), data=self.rideOffer)
        self.assertEqual(res.status_code, 201) #POST request on test ride offers

        res = self.client().get(self.full_url('users/ride_offers/1'))
        self.assertEqual(res.status_code,200)

    def test_user_can_join_a_ride_offer(self):
        """Test user can join ride offers"""
        res = self.client().post(self.full_url('users/ride_offers'), data=self.rideOffer)
        self.assertEqual(res.status_code, 201) #POST ride offer

        res = self.client().get(self.full_url('users/ride_offers/1/join'))
        self.assertEqual(res.status_code,201) #joined ride offer

    def test_user_can_see_joined_ride_offers(self):
        """Test whether users can see ride offers he/she has joined"""
        res = self.client().post(self.full_url('users/ride_offers'), data=self.rideOffer)
        self.assertEqual(res.status_code, 201) #POST ride offer

        res = self.client().get(self.full_url('users/ride_offers/joined'))
        self.assertEqual(res.status_code,200) #joined ride offer
          

    

