from flask import Flask, render_template
from lib.biblioteca_garoafa import descriere_garoafa, culoare_garoafa, anotimp_garoafa



app = Flask(__name__)

@app.route("/")
def index():
    descriere = descriere_garoafa()
    culoare = culoare_garoafa()
    anotimp = anotimp_garoafa()

    return render_template("garoafa.html", descriere = descriere, culoare = culoare, anotimp = anotimp)

if __name__ == "__main__":
    app.run()




    