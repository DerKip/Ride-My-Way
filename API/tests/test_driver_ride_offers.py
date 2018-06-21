from tests.base_test import BaseTestCase
import json

class DriverTestCase(BaseTestCase):
    """This class represents Driver requests test case"""

    def setUp(self):
        """Defining the test variable and initializing the app"""
        super().setUp()
        self.rideOffer={
                        "destination":"Westlands",
                        "from_location":"Pumu",
                        "departure_time":"10:30",
                        "price":"300"
                        }
        
    def test_driver_can_create_ride_offer(self):
        """Test driver can create a ride offer (POST request)"""
        res = self.client().post(self.full_url('driver/create_ride'), data=json.dumps(dict(self.rideOffer)),
        content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_driver_can_get_all_rides_offers(self):
        """Test driver can get all ride offer (GET request)"""
        res = self.client().post(self.full_url('driver/create_ride'), data=json.dumps(dict(self.rideOffer)),
        content_type='application/json')
        self.assertEqual(res.status_code, 201)

        res = self.client().get(self.full_url('driver/rides'))
        self.assertEqual(res.status_code, 200) 

    def test_driver_can_get_a_single_ride_offer(self):
        """Test driver can get a ride offer by id (GET request)"""
        res = self.client().post(self.full_url('driver/ride'), data=self.rideOffer)
        self.assertEqual(res.status_code, 201) #POST request on test ride offers

        res = self.client().get(self.full_url('driver/ride_offers/1'))
        self.assertEqual(res.status_code,200)
    
    def test_driver_can_see_created_ride_offers(self):
        """Test whether a driver can see ride offers he/she has created"""
        res = self.client().post(self.full_url('driver/ride_offers'), data=self.rideOffer)
        self.assertEqual(res.status_code, 201) #POST ride offer

        res = self.client().get(self.full_url('driver/ride_offers/created'))
        self.assertEqual(res.status_code,200) #joined ride offer
          
    
        

    

