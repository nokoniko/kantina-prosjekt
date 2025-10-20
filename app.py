from flask import Flask, render_template
from utils.hjelp import Hjelp
from utils.liste import *

# ---- klasser ----
app = Flask(__name__)
hjelp = Hjelp(__name__)
liste = Liste(__name__)

# --- route til nettsider ---

@app.route('/')
def index() -> str:
    return render_template('hjem/index.html')

@app.route('/meny')
def meny() -> str:
    return render_template('kantine/meny.html', menyen=liste.menyen)

@app.route('/kontakt')
def kontakt() -> str:
    return render_template('kantine/kontakt.html', kontakter=liste.kontanktpersoner)

@app.route('/varer')
def varer() -> str:
    return render_template('kantine/varer.html', varere=liste.varere)

@app.route('/dagmeny')
def dagens() -> str:
    return hjelp.dagmeny()


@app.route('/rett/<slug>')
def rett(slug: str) -> str:
    # Viser enkel detaljside for rett basert på slug, koblet til templates/retter/<slug>.html
    return render_template(f'retter/{slug}.html')

# gjører
if __name__ == "__main__":
    app.run(debug=True)