import unittest
from app.trandafir import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()


    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Plumiera', response.data)

    def test_description_page(self):
        response = self.app.get('/descriere', follow_redirects=True)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Plumiera', response.data)

    def test_photo_page(self):
        response = self.app.get('/poze', follow_redirects=True)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Plumiera', response.data)


if __name__ == "_main_":
    unittest.main()