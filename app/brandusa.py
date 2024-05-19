from flask import Flask, url_for, render_template
import lib.libs

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/brandusa", methods=['GET'])
def brandusa():
    descriere = lib.libs.descriere_brandusa()
    culoare = lib.libs.culoare_brandusa()
    return render_template("brandusa.html", descriere=descriere, culoare=culoare)

@app.route("/brandusa/descriere", methods=['GET'])
def descriere_brandusa():
    descriere = lib.libs.descriere_brandusa()
    return render_template("descriere.html", descriere=descriere)

@app.route("/brandusa/culoare", methods=['GET'])
def culoare_brandusa():
    culoare = lib.libs.culoare_brandusa()
    return render_template("culoare.html", culoare=culoare)

if __name__ == "__main__":
    app.run(debug=True)