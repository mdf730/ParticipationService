import unittest
import requests
import json

class TestStudents(unittest.TestCase):

	PORT_NUM = '51029'
	print("Testing Port number: ", PORT_NUM)
	SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
	CLASS_URL = SITE_URL + '/class/'
	RESET_URL = SITE_URL + '/reset/'

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False

	def reset_data(self):
		m = {}
		r = requests.put(self.RESET_URL, data = json.dumps(m))

	def test_class_get(self):
		self.reset_data()
		r = requests.get(self.CLASS_URL)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(len(resp['classes']), 5)
	
	def test_class_key_get(self):	
		self.reset_data()
		cid = "3"
		r = requests.get(self.CLASS_URL + cid)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(len(resp['students']), 7)

	def test_class_put(self):
		self.reset_data()
		cid = "3"
		r = requests.get(self.CLASS_URL + cid)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(len(resp['students']), 7)

		c = {}
		c["name"] = "Math"
		c["prof"] = "Prof. Obama"
		c["point_goal"] = 100
		c["students"] = [1]
		r = requests.put(self.CLASS_URL + str(cid), data = json.dumps(c))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.CLASS_URL + cid)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(len(resp['students']), len(c["students"]))
	
	def test_class_delete(self):
		self.reset_data()
		cid = "3"
		m = {}
		r = requests.delete(self.CLASS_URL + str(cid), data = json.dumps(m))
		self.assertTrue(self.is_json(r.content))
		resp = json.loads(r.content)
		self.assertEquals(resp['result'], 'success')
		
if __name__ == "__main__":
	unittest.main()
