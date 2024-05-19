import unittest
from ..app.lib.biblioteca_margareta import descriere_margareta, culoare_margareta


class TestBiblioteca(unittest.TestCase):

    def testdescrieremargareta(self):
        descriere = descriere_margareta()
        self.assertEqual(descriere,
                         "Margaretele sunt flori de camp, care pot fi intalnite frecvent pe pasuni si pajisti.")

    def test_culoare_margareta(self):
        culoare = culoare_margareta()
        self.assertEqual(culoare, "Margareta este de obicei de culoare alba.")


if __name__ == "__main__":
    unittest.main()