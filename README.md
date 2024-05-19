# Curs_CVGJ_24_flori
Acesta este un proiect simplu Flask care servește pagini web pentru a descrie floarea Plumeria. Aplicația are trei rute: o pagină principală, o pagină de descriere și o pagină de poze.

## Cerințe

- Python 3.x
- Flask

## Instalare

1. Clonează acest repository:

    bash
    git clone https://github.com/StateAnelice/Curs_CVGJ_24_flori.git
    

2. Creează și activează un mediu virtual:

    bash
    python -m venv venv
    source venv/bin/activate   # Pentru Linux/macOS
    venv\Scripts\activate      # Pentru Windows
    

3. Instalează dependințele necesare:

    bash
    pip install Flask
    

## Structura Proiectului

Asigură-te că ai următoarea structură de directoare și fișiere:


- app.py: Conține codul sursă pentru aplicația Flask.
- templates/: Director care conține fișierele HTML pentru paginile servite.

## Utilizare

1. Rulează aplicația Flask:

    bash
    python plumiera.py
    

2. Accesează aplicația în browser la următoarele URL-uri:

    - Pagina principală: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    - Pagina de descriere: [http://127.0.0.1:5000/descriere](http://127.0.0.1:5000/descriere)
    - Pagina de poze: [http://127.0.0.1:5000/poze](http://127.0.0.1:5000/poze)

## Codul

```python
import sys
from flask import Flask, url_for, render_template

app = Flask(_name_)

@app.route("/")
def index():
    return render_template('plumeria.html')

@app.route("/descriere")
def descriere():
    return render_template('desc_plum.html')

@app.route("/poze")
def poze():
    return render_template('poze_plum.html')

if _name_ == "_main_":
    app.run(debug=True)