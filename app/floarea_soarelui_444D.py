from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/color")
def color():
    return render_template("color.html")

@app.route("/description")
def description():
    return render_template("description.html")

if __name__== '__main__':
    app.run(debug=True)