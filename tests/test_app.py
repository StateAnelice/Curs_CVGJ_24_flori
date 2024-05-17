import unittest
from brandusa import brandusa

class BasicTests(unittest.TestCase):

    def setUp(self):
        # create a test client
        self.brandusa = brandusa.test_client()
        # propagate the exceptions to the test client
        self.brandusa.testing = True

    def test_index(self):
        # sends HTTP GET request to the brandusalication
        result = self.brandusa.get('/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Flori', result.data)

    def test_brandusa(self):
        result = self.brandusa.get('/brandusa')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Brândușa de munte', result.data)

    def test_brandusa_descriere(self):
        result = self.brandusa.get('/brandusa/descriere')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Descriere', result.data)

    def test_brandusa_culoare(self):
        result = self.brandusa.get('/brandusa/culoare')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Culoare', result.data)

if __name__ == "__main__":
    unittest.main()
