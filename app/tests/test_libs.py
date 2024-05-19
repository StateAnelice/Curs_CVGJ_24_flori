import unittest
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib')))

from biblioteca_panseluta import descriere_panseluta, culoare_panseluta, anotimp_panseluta

class TestBibliotecaPanseluta(unittest.TestCase):
    def test_descriere_panseluta(self):
        self.assertEqual(descriere_panseluta(), "Panseluța este o floare sălbatică de origine europeană, care crește în toate anotimpurile. Panseluța este o plantă de dimensiuni mici, care crește pe tulpină, atinge cel mult 15 cm în înălțime, cu flori care au un diametru de aproximativ 1.5 cm.")

    def test_culoare_panseluta(self):
        self.assertEqual(culoare_panseluta(), "Florile pot fi purpurii, albastre, galbene sau albe.")

    def test_anotimp_panseluta(self):
        self.assertEqual(anotimp_panseluta(), "Panselutele înfloresc de obicei în două anotimpuri: primavara și toamna.")

if __name__ == '__main__':
    unittest.main()
