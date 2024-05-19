import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from garoafa import app as garoafa

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.garoafa = garoafa.test_client()
        self.garoafa.testing = True

    def test_index(self):
        result = self.garoafa.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Despre Garoafa', result.data)

if __name__ == "__main__":
    unittest.main()
