from flask import Flask, url_for

from lib.biblioteca_flori import descriere_Dalia,culoare_Dalia



app = Flask(__name__)





@app.route("/", methods=['GET'])



def index():

	ret = "<h1> Flori </h1>"

	ret += f"<a href={url_for('Dalia')}>Dalia -Iancu Alex-Cristian</a>"

	return ret



@app.route("/Dalia", methods=['GET'])

def Dalia():

	descriere = descriere_Dalia()

	culoare = culoare_Dalia()

	

	ret = "<h1>Dalia</h1>"

	

	ret += f"<a href={url_for('index')}>[Flori]</a>"

	ret += f"<a href={url_for('descriere')}>[Descriere]</a>"

	ret += f"<a href={url_for('culoare')}>[Culoare]</a>"

	

	ret += "<h2>Descriere: </h2>"

	ret += descriere

	

	ret += "<h2>Culoare: </h2>"

	ret+= culoare

	

	return ret



@app.route("/Dalia/descriere", methods=['GET'])

def descriere():



	descriere = descriere_Dalia()

	

	ret = f"<a href={url_for('index')}>[Flori]</a>"

	ret += f"<a href={url_for('Dalia')}>[Dalia]</a>"

	ret += f"<a href={url_for('culoare')}>[Culoare]</a>"

	

	ret += "<h2>Descriere: </h2>"

	ret += descriere

	

	return ret

	

@app.route("/Dalia/culoare", methods=['GET'])

def culoare():

	culoare = culoare_Dalia()

		

	ret = f"<a href={url_for('index')}>[Flori]</a>"

	ret += f"<a href={url_for('Dalia')}>[Dalia]</a>"

	ret += f"<a href={url_for('descriere')}>[Descriere]</a>"

	ret += "<h2>Culoare: </h2>"
