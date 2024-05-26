from flask import Flask, render_template
from biblioteca_narcisa import descriere_narcisa, frunze_narcisa, floare_narcisa, culoare_narcisa
app = Flask (__name__)

@app.route('/')
def index():
    descriere = descriere_narcisa()
    frunze = frunze_narcisa()
    floare = floare_narcisa()
    culoare = culoare_narcisa()

    return render_template('index.html', descriere = descriere, frunze = frunze, floare = floare, culoare = culoare)

if __name__ == '__main__':

    app.run()