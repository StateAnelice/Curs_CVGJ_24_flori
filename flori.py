import sys

from flask import Flask, url_for







print('filme')



app = Flask(__name__)

@app.route("/", methods=['GET'])

def index():

    ret = ""

    ret = "<h>flori</h>"

    

    ret += "<pre>"



    ret += " - -test1"

    ret += " - -test2"

    

    ret += "</pre>"

    ret += " - -test3\n"

    ret += " - -test4"

        

    return ret