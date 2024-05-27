from flask import Flask, url_for
from lib.biblioteca_flori import *

app = Flask(__name__)

@app.route("/", methods=['GET'])

def index():
    ret = "<h1> Flori </h1>"
    ret += f"<a href={url_for('margareta')}>Margareta - Conache Antonio-Mihaita</a>"
    return ret

@app.route("/margareta", methods=['GET'])

def margareta():
    descriere = descriere_margareta()
    culoare = culoare_margareta()

    ret = "<h1> Margareta </h1>"

    ret += f"<a href={url_for('index')}>[Flori]</a>"
    ret += f"<a href={url_for('descriere')}>[Descriere]</a>"
    ret += f"<a href={url_for('culoare')}>[Culoare]</a>"

    ret += "<h2>Descriere: </h2>"
    ret += descriere

    ret += "<h2>Culoare: </h2>"
    ret += culoare

    return ret

@app.route("/margareta/descriere", methods=['GET'])
def descriere():

    descriere = descriere_margareta()

    ret = f"<a href={url_for('index')}>[Flori]</a>"
    ret += f"<a href={url_for('margareta')}>[Margareta]</a>"
    ret += f"<a href={url_for('culoare')}>[Culoare]</a>"

    ret += "<h2>Descriere: </h2>"
    ret += descriere

    return ret

@app.route("/margareta/culoare", methods=['GET'])
def culoare():

    culoare = culoare_margareta()

    ret = f"<a href={url_for('index')}>[Flori]</a>"

    ret += f"<a href={url_for('margareta')}>[Margareta]</a>"
    ret += f"<a href={url_for('descriere')}>[Descriere]</a>"
    ret += f"<h2>Culoare: </h2>"
    ret += culoare
    
    return ret