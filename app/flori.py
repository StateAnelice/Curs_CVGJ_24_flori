import sys

from flask import Flask, url_for
from lib.biblioteca_flori import *


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
	ret = ""
	ret = "<h> Flori </h>"
	
	return ret
@app.route("/lavanda", methods=['GET'])
def lavanda():
	descriere = descriere_lavanda()
	culoare = culoare_lavanda()
	
	ret = "<h1> Lavanda </h1>"
	
	ret += f"<a href={url_for('index')}>[Flori]</a>"
	ret += f"<a href={url_for('descriere')}>[Descriere]</a>"
	ret += f"<a href={url_for('culoare')}>[Culoare]</a>"
	
	ret += "<h2>Descriere: </h2>"
	ret += descriere
	
	ret += "<h2>Culoare: </h2>"
	ret += culoare
	
	return ret

@app.route("/lavanda/descriere", methods=['GET'])
def descriere():
	descriere = descriere_lavanda()
	
	ret = f"<a href={url_for('index')}>[Flori]</a>"
	ret += f"<a href={url_for('descriere')}>[Lavanda]</a>"
	ret += f"<a href={url_for('culoare')}>[Culoare]</a>"
	
	ret += "<h2>Descriere: </h2>"
	ret += descriere
	
	return ret
	
@app.route("/lavanda/culoare", methods=['GET'])
def culoare():
	culoare = culoare_lavanda()
	
	ret = f"<a href={url_for('index')}>[Flori]</a>"
	ret += f"<a href={url_for('descriere')}>[Lavanda]</a>"
	ret += f"<a href={url_for('culoare')}>[Descriere]</a>"
	
	ret += "<h2>Descriere: </h2>"
	ret += descriere
	
	return ret
	
app.run(host = "127.0.0.1", port = 5002)
