import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.biblioteca_garoafa import descriere_garoafa, culoare_garoafa, anotimp_garoafa

class TestBiblioteca(unittest.TestCase):

    def test_descriere_garoafa(self):
        descriere = descriere_garoafa()
        self.assertEqual(descriere, "Garoafa (Dianthus caryophyllus) este o plantă erbacee aparținând familiei Caryophyllaceae. Tulpina ajunge la 1 metru înălțime, are frunzele înguste și ascuțite dispuse în opoziție și flori ce pot avea o gamă amplă de culori")

    def test_culoare_garoafa(self):
        culoare = culoare_garoafa()
        self.assertEqual(culoare, "Garoafele pot fi de culoare alb, roz, roșu, mov, galben.")

    def test_anotimp_garoafa(self):
        anotimp = anotimp_garoafa()
        self.assertEqual(anotimp, "Garoafele înfloresc în general din primăvară până toamna, cu o perioadă principală de înflorire în lunile mai-iulie.")

if __name__ == "__main__":
    unittest.main()
