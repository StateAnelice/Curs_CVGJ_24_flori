import unittest
from app.lacramioara import app

class BasicTests(unittest.TestCase):
    # Executat înainte de fiecare test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    # Verifică că pagina principală se încarcă corect
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Lacramioara', response.data)

    def test_color_page(self):
        response = self.app.get('/color', follow_redirects=True)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Lacramioara', response.data)

    def test_description_page(self):
        response = self.app.get('/description', follow_redirects=True)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Lacramioara', response.data)


# Permite rularea testelor cu 'python test_app.py'
if __name__ == "_main_":
    unittest.main()