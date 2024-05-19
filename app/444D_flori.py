from flask import Flask, url_for
from lib.biblioteca_flori import *

app = Flask(__name__)


@app.route("/", methods=['GET'])

def index():
	ret = "<h1> Flori </h1>"
	ret += f"<a href={url_for('lalea')}>Lalea -State Anelice-Mariana</a>"
	return ret

@app.route("/lalea", methods=['GET'])
def lalea():
	descriere = descriere_lalea()
	culoare = culoare_lalea()
	
	ret = "<h1>Lalea</h1>"
	
	ret += f"<a href={url_for('index')}>[Flori]</a>"
	ret += f"<a href={url_for('descriere')}>[Descriere]</a>"
	ret += f"<a href={url_for('culoare')}>[Culoare]</a>"
	
	ret += "<h2>Descriere: </h2>"
	ret += descriere
	
	ret += "<h2>Culoare: </h2>"
	ret+= culoare
	
	return ret

@app.route("/lalea/descriere", methods=['GET'])
def descriere():

	descriere = descriere_lalea()
	
	ret = f"<a href={url_for('index')}>[Flori]</a>"
	ret += f"<a href={url_for('lalea')}>[Lalea]</a>"
	ret += f"<a href={url_for('culoare')}>[Culoare]</a>"
	
	ret += "<h2>Descriere: </h2>"
	ret += descriere
	
	return ret
	
@app.route("/lalea/culoare", methods=['GET'])
def culoare():
	culoare = culoare_lalea()
		
	ret = f"<a href={url_for('index')}>[Flori]</a>"
	ret += f"<a href={url_for('lalea')}>[Lalea]</a>"
	ret += f"<a href={url_for('descriere')}>[Descriere]</a>"
	ret += "<h2>Culoare: </h2>"
	ret += culoare
	return ret


	

