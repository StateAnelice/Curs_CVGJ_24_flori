import unittest
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib')))

from biblioteca_magnolia import descriere_magnolia, culoare_magnolia, anotimp_magnolia

class TestBibliotecaPanseluta(unittest.TestCase):
    def test_descriere_panseluta(self):
        self.assertEqual(descriere_magnolia(), "Magnolia is a large genus of about 210 to 340 flowering plant species in the subfamily Magnolioideae of the family Magnoliaceae. The natural range of Magnolia species is disjunct, with a main center in east and southeast Asia and a secondary center in eastern North America, Central America, the West Indies, and some species in South America.")
    def test_culoare_panseluta(self):
        self.assertEqual(culoare_magnolia(), "Magnolias are spreading evergreen or deciduous trees or shrubs characterised by large fragrant flowers, which may be bowl-shaped or star-shaped, in shades of white, pink, purple, green, or yellow.")

    def test_anotimp_panseluta(self):
        self.assertEqual(anotimp_magnolia(), "In deciduous species, the blooms often appear before the leaves in spring. Cone-like fruits are often produced in the autumn.")

if __name__ == '__main__':
    unittest.main()
