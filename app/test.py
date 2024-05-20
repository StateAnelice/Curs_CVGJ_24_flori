import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



import sys
sys.path.append("../")



import lib.biblioteca_flori as flori



def test_culoare_orhidee():
	culoare = flori.culoare_lavanda()
	
	if"Florile pot avea culoarea violet închis sau albă." in culoare:
		logger.info(f"Functia culoare_orhidee functioneaza corect: {culoare}")
		assert True
	else:
		logger.error(f"Functia culoare_orhidee NU functioneaza corect: {culoare}")
		assert False



def test_descriere_orhidee():
	descriere = flori.descriere_lavanda()
	
	if "Lavanda este un gen de plante din familia Lamiaceae" in descriere:
		logger.info(f"Functia descriere_orhidee functioneaza corect:\n{descriere}")
		assert True
	else:
		logger.error(f"Functia descriere_orhidee NU functioneaza corect:\n{descriere}")
		assert False
