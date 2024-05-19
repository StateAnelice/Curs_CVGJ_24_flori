import sys

from flask import Flask, url_for , render_template


app = Flask(__name__)

@app.route("/")

def index():
    return render_template('zambila.html')

@app.route("/descriere")

def descriere():
    return render_template('descriere_zambila.html')

@app.route("/poze")

def poze():
    return render_template('poze_zambila.html')
