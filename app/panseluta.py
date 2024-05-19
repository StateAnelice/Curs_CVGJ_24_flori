from flask import Flask, render_template
from lib.biblioteca_panseluta import descriere_panseluta, culoare_panseluta, anotimp_panseluta

app = Flask(__name__)

@app.route('/')
def home():
    descriere = descriere_panseluta()
    culoare = culoare_panseluta()
    anotimp = anotimp_panseluta()
    return render_template('panseluta.html', descriere=descriere, culoare=culoare, anotimp=anotimp)

if __name__ == '__main__':
    app.run(debug=True)
