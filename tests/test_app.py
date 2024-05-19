import unittest
from app.liliac import liliac

class BasicTests(unittest.TestCase):

    def setUp(self):
        # create a test client
        self.liliac = liliac.test_client()
        # propagate the exceptions to the test client
        self.liliac.testing = True

    def test_index(self):
        # sends HTTP GET request to the liliaclication
        result = self.liliac.get('/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Flori', result.data)


    def test_brandusa_descriere(self):
        result = self.brandusa.get('/descriere')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Descriere', result.data)

    def test_brandusa_frunze(self):
        result = self.brandusa.get('/frunze')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Frunze', result.data)

    def test_brandusa_floare(self):
        result = self.brandusa.get('/floare')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Floare', result.data)


    def test_brandusa_culoare(self):
        result = self.brandusa.get('/culoare')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Culoare', result.data)

if __name__ == "__main__":
    unittest.main()
