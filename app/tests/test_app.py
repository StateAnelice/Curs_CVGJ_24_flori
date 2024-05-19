import unittest

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bujori import app as bujori

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.bujori = bujori.test_client()
        self.bujori.testing = True

    def test_index(self):
        result = self.bujori.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'index', result.data)

if __name__ == "__main__":
    unittest.main()
