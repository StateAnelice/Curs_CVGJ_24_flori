import unittest
from lib.libs import descriere_brandusa, culoare_brandusa

class TestBiblioteca(unittest.TestCase):

    def test_descriere_brandusa(self):
        descriere = descriere_brandusa()
        self.assertEqual(descriere, "Brândușa de munte este o plantă perenă, cu flori violete sau albe, care crește în regiunile montane.")

    def test_culoare_brandusa(self):
        culoare = culoare_brandusa()
        self.assertEqual(culoare, "Florile brândușei de munte sunt de obicei violete, dar pot fi și albe.")

if __name__ == "__main__":
    unittest.main()
