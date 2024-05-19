import unittest

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.biblioteca_bujori import descriere_bujori, culoare_bujori, anotimp_bujori

class TestBiblioteca(unittest.TestCase):

    def test_descriere_bujori(self):
        descriere = descriere_bujori()
        self.assertEqual(descriere, "Bujorii (Paeonia) sunt flori de grădină extrem de populare, apreciate pentru florile lor mari și parfumate. \n Bujorii sunt plante perene care aparțin familiei Paeoniaceae. Sunt originari din Asia, Europa și America de Nord și sunt cunoscuți pentru florile lor spectaculoase și frunzișul luxuriant")

    def test_culoare_brandusa(self):
        culoare = culoare_bujori()
        self.assertEqual(culoare, "Bujorii pot fi de culoare alb, roz, roșu, mov, galben, ultimele două fiind mai rar întâlnite")

    def test_anotimp_bujori(self):
        anotimp = anotimp_bujori()
        self.assertEqual(anotimp, "Bujorii înfloresc în principal primăvara și la începutul verii, începând cu luna mai")

if __name__ == "__main__":
    unittest.main()
