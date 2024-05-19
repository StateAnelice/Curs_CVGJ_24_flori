import unittest
from app.lib.margareta import margareta

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.margareta = margareta.test_client()
        self.margareta.testing = True

    def test_index(self):
        result = self.margareta.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Index', result.data)

if __name__ == "__main__":
    unittest.main()