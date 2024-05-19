import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

import lib.biblioteca_flori as flori



def test_culoare_lalea():
    culoare = flori.culoare_lalea()

    if "Delphinidin dă florii culoare violet" in culoare:
        logger.info(f"Functia culoare_lalea functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_lalea NU functioneaza corect: {culoare}")
        assert False

def test_descriere_lalea():
    descriere = fructe.descriere_lalea()

    if "Laleaua este o planta bulboasa perena" in descriere:
        logger.info(f"Functia descriere_lalea functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_lalea NU functioneaza corect:\n{descriere}")
        assert False 
