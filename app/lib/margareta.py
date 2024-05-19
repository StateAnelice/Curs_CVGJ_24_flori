from flask import Flask, render_template
from biblioteca_margareta import descriere_margareta, culoare_margareta

app = Flask(__name__)

@app.route('/')
def index():
    descriere = descriere_margareta()
    culoare = culoare_margareta()

    return render_template('index.html', descriere=descriere, culoare=culoare)

if __name__ == '__main__':

    app.run()