import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

import lib.biblioteca_flori as flori



def test_culoare_Dalia():
    culoare = flori.culoare_Dalia()

    if "toate culorile" in culoare:
        logger.info(f"Functia culoare_Dalia functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_Dalia NU functioneaza corect: {culoare}")
        assert False

def test_descriere_Dalia():
    descriere = flori.descriere_acai()

    if "plus de culoare" in descriere:
        logger.info(f"Functia descriere_Dalia functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_Dalia NU functioneaza corect:\n{descriere}")
        assert False 
