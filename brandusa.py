from flask import Flask, url_for
from lib.libs import descriere_brandusa, culoare_brandusa


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = "<h1> Flori </h1>"
    ret += f"<a href={url_for('brandusa')}>Brândușa de munte -State Anelice-Mariana</a>"
    return ret

@app.route("/brandusa", methods=['GET'])
def brandusa():
    descriere = descriere_brandusa()
    culoare = culoare_brandusa()
    
    ret = "<h1>Brândușa de munte</h1>"
    
    ret += f"<a href={url_for('index')}>[Flori]</a>"
    ret += f"<a href={url_for('descriere_brandusa')}>[Descriere]</a>"
    ret += f"<a href={url_for('culoare_brandusa')}>[Culoare]</a>"
    
    ret += "<h2>Descriere: </h2>"
    ret += descriere
    
    ret += "<h2>Culoare: </h2>"
    ret += culoare
    
    return ret

@app.route("/brandusa/descriere", methods=['GET'])
def descriere_brandusa():
    descriere = descriere_brandusa()
    
    ret = f"<a href={url_for('index')}>[Flori]</a>"
    ret += f"<a href={url_for('brandusa')}>[Brândușa de munte]</a>"
    ret += f"<a href={url_for('culoare_brandusa')}>[Culoare]</a>"
    
    ret += "<h2>Descriere: </h2>"
    ret += descriere
    
    return ret
    
@app.route("/brandusa/culoare", methods=['GET'])
def culoare_brandusa():
    culoare = culoare_brandusa()
        
    ret = f"<a href={url_for('index')}>[Flori]</a>"
    ret += f"<a href={url_for('brandusa')}>[Brândușa de munte]</a>"
    ret += f"<a href={url_for('descriere_brandusa')}>[Descriere]</a>"
    ret += "<h2>Culoare: </h2>"
    ret += culoare
    return ret

if __name__ == "__main__":
    app.run(debug=True)
