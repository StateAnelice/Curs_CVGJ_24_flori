from flask import Flask, url_for
from lib.biblioteca_flori import *

app = Flask(__name__)


@app.route("/", methods=['GET'])

def index():
	ret = "<h1> Flori </h1>"
	ret += f"<a href={url_for('papadie')}>Papadie -Dutu Marius Valentin</a>"
	return ret

@app.route("/papadie", methods=['GET'])
def papadie():
	descriere = descriere_papadie()
	culoare = culoare_papadie()
	
	ret = "<h1>Papadie</h1>"
	
	ret += f"<a href={url_for('index')}>[Flori]</a>"
	ret += f"<a href={url_for('descriere')}>[Descriere]</a>"
	ret += f"<a href={url_for('culoare')}>[Culoare]</a>"
	
	ret += "<h2>Descriere: </h2>"
	ret += descriere
	
	ret += "<h2>Culoare: </h2>"
	ret+= culoare
	
	return ret

@app.route("/papadie/descriere", methods=['GET'])
def descriere():

	descriere = descriere_papadie()
	
	ret = f"<a href={url_for('index')}>[Flori]</a>"
	ret += f"<a href={url_for('papadie')}>[Papadie]</a>"
	ret += f"<a href={url_for('culoare')}>[Culoare]</a>"
	
	ret += "<h2>Descriere: </h2>"
	ret += descriere
	
	return ret
	
@app.route("/papadie/culoare", methods=['GET'])
def culoare():
	culoare = culoare_papadie()
		
	ret = f"<a href={url_for('index')}>[Flori]</a>"
	ret += f"<a href={url_for('papadie')}>[Papadie]</a>"
	ret += f"<a href={url_for('descriere')}>[Descriere]</a>"
	ret += "<h2>Culoare: </h2>"
	ret += culoare
	return ret


	
