from flask import Flask, render_template, request, redirect, url_for, flash
from utils.hjelp import Hjelp
from utils.liste import *
from utils.forms import *
# ---- klasser ----
app = Flask(__name__)
app.secret_key = 'supersecretkey'
hjelp = Hjelp(__name__)
liste = Liste(__name__)
forms = Forms(__name__)

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

@app.route('/tilbakemelding', methods=['GET', 'POST'])
def tilbakemelding():
    if request.method == 'POST':
        navn = request.form['navn']
        melding = request.form['melding']
        forms.save_message(navn, melding)
        flash("Takk for tilbakemeldingen! 😊")
        return redirect(url_for('tilbakemelding'))
    return forms.vis_tilbakemeldinger()

# gjører
if __name__ == "__main__":
    app.run(debug=True)