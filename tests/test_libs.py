import unittest
from apps.lib.libs import descriere_ghiocel, culoare_ghiocel


class TestBiblioteca(unittest.TestCase):

    def test_descriere_ghiocel(self):
        descriere = descriere_ghiocel()
        self.assertEqual(descriere,
                         "Ghiocelul (Galanthus L.; din limba greaca: gala - lapte, anthos - floare) este un gen de aproximativ 20 de specii de plante erbacee perene bulboase din familia Amaryllidaceae, plante care înfloresc printre primele la începutul primăverii. Plantele au două frunze liniare și o singură floare mică, albă, care atârnă în formă de clopot, cu șase petale în două cercuri ( verticil). Petalele interioare mai mici au semne verzi")

    def test_culoare_ghiocel(self):
        culoare = culoare_ghiocel()
        self.assertEqual(culoare, "Ghiocelul e de obicei alb")


if __name__ == "__main__":
    unittest.main()