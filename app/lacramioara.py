from flask import Flask, url_for, render_template
import lib.libs

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/lacramioara", methods=['GET'])
def lacramioara():
    descriere = lib.libs.descriere_lacramioara()
    culoare = lib.libs.culoare_lacramioara()
    return render_template("lacramioara.html", descriere=descriere, culoare=culoare)

@app.route("/lacramioara/descriere", methods=['GET'])
def descriere_lacramioara():
    descriere = lib.libs.descriere_lacramioara()
    return render_template("descriere.html", descriere=descriere)

@app.route("/lacramioara/culoare", methods=['GET'])
def culoare_lacramioara():
    culoare = lib.libs.culoare_lacramioara()
    return render_template("culoare.html", culoare=culoare)

if __name__ == "__main__":
    app.run(debug=True)