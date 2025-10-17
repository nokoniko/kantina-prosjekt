from flask import Flask, render_template
from utils.hjelp import Hjelp
from utils.liste import *

app = Flask(__name__)
hjelp = Hjelp(__name__)
liste = Liste(__name__)


@app.route('/')
def index() -> str:
    return render_template('index.html')

@app.route('/meny')
def meny() -> str:
    return render_template('meny.html', menyen=liste.menyen)

@app.route('/kontakt')
def kontakt() -> str:
    return render_template('kontakt.html')

@app.route('/varer')
def varer() -> str:
    return render_template('varer.html', varere=liste.varere)

@app.route('/dagmeny')
def dagens() -> str:
    return render_template('dagens.html')

if __name__ == "__main__":
    app.run(debug=True)