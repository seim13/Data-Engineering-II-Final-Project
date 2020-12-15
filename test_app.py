import unittest
import os
import requests
from app import app 

class FlaskTests(unittest.TestCase):

	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
	
		
	def tearDown(self):
		pass
	
	
	def test_server_is_up(self):
		responce = requests.get('http://localhost:5000')
		self.assertEqual(responce.status_code, 200)
	  
	  
	  if __name__ == '__main__':
		unittest.main()	
