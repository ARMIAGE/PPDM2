from flask import Flask, request, render_template
app = Flask(__name__)
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import word2vec
import file_insertion
import similarity
import warnings
import argparse

model = word2vec.Word2Vec.load('../MODEL/W2V_text8_Model.bin')

@app.context_processor
def titre():
    return dict(titre="Word Embedding Application")

@app.route('/')
def accueil():
    typeFichier = ["Cos Matrix BRM IFR", "MC", "MTURK-771", "rel122-norms", "RG", "SimLex-999", "WordSim", "Autre fichier"]
    return render_template('accueil.html', typeFichier=typeFichier)

@app.route('/resultat')
def resultat():
    File = request.args.get('file')
    if File == "RG":
        resultat = similarity.similarite(model, file_insertion.insert_file_rg())
    elif File == "Cos Matrix BRM IFR":
        resultat = similarity.similarite(model, file_insertion.insert_file_cos_matrix_brm_ifr())
    else:
        File = "Not Found"
    return render_template('similarite_resultats.html', File=File, resultat=resultat)

@app.errorhandler(404)
def ma_page_404(error):
    return "Page non trouvée. Erreur ", 404


if __name__ == '__main__':
    app.run(debug=True)
