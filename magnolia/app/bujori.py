from flask import Flask, render_template
from lib.biblioteca_bujori import descriere_bujori, culoare_bujori, anotimp_bujori



app = Flask(__name__)

@app.route("/")
def index():
    descriere = descriere_bujori()
    culoare = culoare_bujori()
    anotimp = anotimp_bujori()

    return render_template("bujori.html", descriere = descriere, culoare = culoare, anotimp = anotimp)

if __name__ == "__main__":
    app.run()




    