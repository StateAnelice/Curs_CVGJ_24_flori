from flask import Flask, url_for , render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("trandafir.html")

@app.route("/descriere")
def descriere_trandafir():
    return render_template('descriere_trandafir.html')

@app.route("/poze")
def poze_trandafir():
    return render_template('poze_trandafir.html')