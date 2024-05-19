import unittest

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from liliac import app as liliac

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.liliac = liliac.test_client()
        self.liliac.testing = True

    def test_liliac_descriere(self):
        result = self.liliac.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Descriere', result.data)

    def test_liliac_frunze(self):
        result = self.liliac.get('/frunze')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Frunze', result.data)

    def test_liliac_floare(self):
        result = self.liliac.get('/floare')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Floare', result.data)


    def test_liliac_culoare(self):
        result = self.liliac.get('/culoare')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Culoare', result.data)

if __name__ == "__main__":
    unittest.main()
