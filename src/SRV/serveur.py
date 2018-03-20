from flask import Flask, request, render_template
from datetime import date
app = Flask(__name__)

@app.context_processor
def passer_titre():
    return dict(titre="Application PPD")
def est_impair(n):
    if n % 2 == 1:
        return True
    return False

@app.route('/')
def index():
    return "Index"

@app.route('/app')
def accueil():
    mots = ["bonjour", "à", "toi,", "visiteur."]
    rep = est_impair(4)
    return render_template('accueil.html', mots=mots, rep=rep)

@app.errorhandler(404)
def ma_page_404(error):
    return "Page non trouvée. Erreur ", 404


if __name__ == '__main__':
    app.run(debug=True)
