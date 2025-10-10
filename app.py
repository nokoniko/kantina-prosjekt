from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    return render_template('index.html')

@app.route('/meny')
def meny() -> str:
    return render_template('meny.html')

@app.route('/kontakt')
def kontakt() -> str:
    return render_template('kontakt.html')

@app.route('/varer')
def varer() -> str:
    return render_template('varer.html')


if __name__ == "__main__":
    app.run(debug=True)
