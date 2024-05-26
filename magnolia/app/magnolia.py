from flask import Flask, render_template
from lib.biblioteca_magnolia import descriere_magnolia, culoare_magnolia, anotimp_magnolia

app = Flask(__name__)

@app.route('/')
def home():
    descriere = descriere_magnolia()
    culoare = culoare_magnolia()
    anotimp = anotimp_magnolia()
    return render_template('magnolia.html', descriere=descriere, culoare=culoare, anotimp=anotimp)

if __name__ == '__main__':
    app.run(debug=True)
