import unittest
from lib.libs import descriere_brandusa, culoare_brandusa

class TestBiblioteca(unittest.TestCase):

    def test_descriere_brandusa(self):
        descriere = descriere_brandusa()
        self.assertEqual(descriere, "Lăcrămioara (lat. Convallaria majalis) este o specie de plante erbacee, perene prin rizom,.")

    def test_culoare_brandusa(self):
        culoare = culoare_brandusa()
        self.assertEqual(culoare, "Florile lăcrămioarei sunt de regulă albe, uneori avand ușoare note rozalii pe margini.")

if __name__ == "__main__":
    unittest.main()
