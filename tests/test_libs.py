import unittest
from app.lib.biblioteca_liliac import descriere_liliac, frunze_liliac, floare_liliac, culoare_liliac

class TestBiblioteca(unittest.TestCase):

    def test_descriere_liliac(self):
        descriere = descriere_liliac()
        self.assertEqual(descriere, "Liliacul (Syringa vulgaris) face parte din familia oleaceelor și este o specie din genul Syringa care înflorește primăvara. Este un arbust a cărui înălțime poate ajunge până la șapte metri, cu ramuri drepte și lujeri puțin muchiați.")

    def test_frunze_liliac(self):
        frunze = culoare_liliac()
        self.assertEqual(frunze, "Frunzele sunt ovate sau lat-ovate, la bază cordate, până la 12 centimetri lungime, acuminate, pețiol circa 2,5 cm lungime, glabre, verzi-întunecat.")

    def test_floare_liliac(self):
        floare = floare_liliac()
        self.assertEqual(floare, "Florile sunt simple sau duble, plăcut mirositoare, grupate în penicule de până la 20 cm lungime, multiflorale, în culori diferite, de la liliachiu la alb. Floarea are caliciul mic, campanulat, cu patru dinți, corolă cu tub de un centimetru lungime, cu patru lobi patenți și două stamine.")

    def test_culoare_liliac(self):
        culoare = culoare_liliac()
        self.assertEqual(culoare, "Lila este o culoare asemănătoare cu violetul, dar o nuanță mai deschisă, spre roz. Numele provine de la florile de liliac, care au această culoare.")

if __name__ == "__main__":
    unittest.main()
