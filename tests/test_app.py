import unittest
from ghiocel import ghiocel

class BasicTests(unittest.TestCase):

    def setUp(self):
        # create a test client
        self.ghiocel = ghiocel.test_client()
        # propagate the exceptions to the test client
        self.ghiocel.testing = True

    def test_index(self):
        # sends HTTP GET request to the ghiocellication
        result = self.ghiocel.get('/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Flori', result.data)

    def test_ghiocel(self):
        result = self.ghiocel.get('/ghiocel')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Ghiocel', result.data)

    def test_ghiocel_descriere(self):
        result = self.ghiocel.get('/ghiocel/descriere')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Descriere', result.data)

    def test_ghiocel_culoare(self):
        result = self.ghiocel.get('/ghiocel/culoare')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Culoare', result.data)

if __name__ == "__main__":
    unittest.main()