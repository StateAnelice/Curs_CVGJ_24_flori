from flask import Flask, render_template
from lib.biblioteca_liliac import descriere_liliac, frunze_liliac, floare_liliac, culoare_liliac
app = Flask(__name__)

@app.route('/')
def index():
    descriere = descriere_liliac()

    return render_template('index.html', descriere=descriere)

@app.route('/frunze')
def frunze():
    frunze = frunze_liliac()

    return render_template('frunze.html', frunze = frunze)

@app.route('/floare')
def floare():
    floare = floare_liliac()

    return render_template('floare.html', floare = floare)

@app.route('/culoare')
def culoare():
    culoare = culoare_liliac()

    return render_template('culoare.html', culoare = culoare)

if __name__ == '__main__':

    app.run()