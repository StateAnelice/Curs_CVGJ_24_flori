import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

import lib.biblioteca_flori as flori



def test_culoare_papadie():
    culoare = flori.culoare_papadie()

    if "galben" in culoare:
        logger.info(f"Functia culoare_papadie functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_papadie NU functioneaza corect: {culoare}")
        assert False

def test_descriere_papadie():
    descriere = flori.descriere_papadie()

    if "este o plantă erbacee" in descriere:
        logger.info(f"Functia descriere_papadie functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_papadie NU functioneaza corect:\n{descriere}")
        assert False 
