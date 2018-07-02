import unittest

from ..app import initialize_app

class BaseTestCase(unittest.TestCase):
    """Set up Base Test Class"""

    url_prefix = '/api/v2/'

    def setUp(self):
        self.app = initialize_app("testing")
        self.client = self.app.test_client  
      
    def full_url(self, path=''):
        """returns the endpoint url for testing"""
        return self.url_prefix + path


    
