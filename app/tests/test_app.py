import unittest

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from panseluta import app as panseluta

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.panseluta = panseluta.test_client()
        self.panseluta.testing = True

    def test_index(self):
        result = self.panseluta.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Despre Panselute', result.data)

if __name__ == "__main__":
    unittest.main()
