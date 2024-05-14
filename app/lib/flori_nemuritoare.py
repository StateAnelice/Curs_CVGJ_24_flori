import sys
import os 

from flask import Flask, url_for , render_template



app = Flask(__name__)

@app.route("/")
def index():
    return render_template('Cioroiu_Diana/index.html')

@app.route("/poze")
def poze():
    return render_template('Cioroiu_Diana/poze.html')

@app.route("/preturi")
def preturi():
    return render_template('Cioroiu_Diana/preturi.html')