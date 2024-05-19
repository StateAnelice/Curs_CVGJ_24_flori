from flask import Flask, url_for, render_template
import lib.libs

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/hortensie", methods=['GET'])
def hortensie():
    descriere = lib.libs.descriere_hortensie()
    culoare = lib.libs.culoare_hortensie()
    return render_template("hortensie.html", descriere=descriere, culoare=culoare)

@app.route("/hortensie/descriere", methods=['GET'])
def descriere_hortensie():
    descriere = lib.libs.descriere_hortensie()
    return render_template("descriere.html", descriere=descriere)

@app.route("/hortensie/culoare", methods=['GET'])
def culoare_hortensie():
    culoare = lib.libs.culoare_hortensie()
    return render_template("culoare.html", culoare=culoare)

if __name__ == "__main__":
    app.run(debug=True)