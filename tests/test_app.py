import unittest
from ghiocel import ghiocel

class BasicTests(unittest.TestCase):



    def test_index(self):
        result = self.ghiocel.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'index', result.data)





if __name__ == "__main__":
    unittest.main()