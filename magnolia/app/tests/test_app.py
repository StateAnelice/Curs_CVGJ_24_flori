import unittest

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from magnolia import app as magnolia

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.magnolia = magnolia.test_client()
        self.magnolia.testing = True

    def test_index(self):
        result = self.magnolia.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Despre Magnolie', result.data)

if __name__ == "__main__":
    unittest.main()
