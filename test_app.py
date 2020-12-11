import unittest
import os
import requests

class FlaskTests(unittest.TestCase):
		
	def tearDown(self):
		pass
	
	
	def test_a_index(self):
		responce = requests.get('http://127.0.0.1:5000/')
		self.assertEqual(responce.status_code, 200)
