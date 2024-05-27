import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append('../')

import lib.biblioteca_flori  as flori

def test_culoare_margareta():
    culoare = flori.culoare_margareta()

    if "Culoarea unei margarete este alba." in culoare:
        logger.info(f"Functia culoare_margareta functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_margareta NU functioneaza corect: {culoare}")
        assert False

def test_descriere_margareta():
    descriere = flori.descriere_margareta()

    if "Margaretele (Leucanthemum vulgare) sunt flori de câmp" in descriere:
        logger.info(f"Functia descriere_margareta functioneaza corect:\n {descriere}")
        assert True
    else:
        logger.info(f"Functia descriere_margareta NU functioneaza corect:\n {descriere}")
        assert False