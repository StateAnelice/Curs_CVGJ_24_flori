from flask import Flask, render_template
from libs import descriere_ghiocel , culoare_ghiocel

app = Flask(__name__)

@app.route('/')
def index():
    descriere = descriere_ghiocel
    culoare = culoare_ghiocel

    return render_template('index.html' , descriere = descriere , culoare = culoare)

    if __name__ == 'main':

        app.run()
        