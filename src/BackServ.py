from flask import Flask, request, render_template
app = Flask(__name__)
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import word2vec
import file_insertion
import similarity
import warnings
import argparse
import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt','csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

model = word2vec.Word2Vec.load('../MODEL/W2V_text8_Model.bin')

@app.context_processor
def titre():
    """
    Cette fonction a pour but d'afficher un titre pour l'interface web de l'application

    :return: Un titre du dictionnaire de données dict
    """
    return dict(titre="Word Embedding Application")

@app.route('/')
def accueil():
    """
    Cette fonction liste dans l'accueil les fichiers sur lesquels on peut effectuer les tests de similarité

    :return: La liste des noms des fichiers sources pour les tests de similarité
    """
    typeFichier = ["MC", "MTURK-771", "rel122-norms", "RG", "SimLex-999", "WordSim", "Cos Matrix BRM IFR"]
    return render_template('accueil.html', typeFichier=typeFichier)

@app.route("/s/upload", methods=['GET', 'POST'])
def s_upload():
    """
    Cette fonction permet de charger un fichier .txt ou .csv format Mot1, Mot2, corrélation afin d'effectuer les tests pour déterminer un coefficient de similarité

    :return: Le coefficent de corrélation correspondant au fichier donné en entrée
    """
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            FileTRT = app.config['UPLOAD_FOLDER'] + "/" + filename
            resultat = similarity.similarite(model, file_insertion.insert_file_generic(FileTRT))
            return render_template('s_resultats.html', File=filename, resultat=round(resultat,5))
    return render_template('s_upload.html')

@app.route('/s/resultat')
def s_resultat():
    """
    Cette fonction donne le résultat de similarité pour les fichiers déjà chargés sur l'interface web

    :return: Le coefficent de corrélation correspondant au fichier sur lequel on clique sur l'interface web
    """
    File = request.args.get('file')
    if File == "RG":
        resultat = similarity.similarite(model, file_insertion.insert_file_rg())
    elif File == "Cos Matrix BRM IFR":
        resultat = similarity.similarite(model, file_insertion.insert_file_cos_matrix_brm_ifr())
    elif File == "MC":
        resultat = similarity.similarite(model, file_insertion.insert_file_mc())
    elif File == "MTURK-771":
        resultat = similarity.similarite(model, file_insertion.insert_file_mturk771())
    elif File == "rel122-norms":
        resultat = similarity.similarite(model, file_insertion.insert_file_rel122())
    elif File == "SimLex-999":
        resultat = similarity.similarite(model, file_insertion.insert_file_simlex999())
    elif File == "WordSim":
        resultat = similarity.similarite(model, file_insertion.insert_file_wordsim())
    else:
        resultat = similarity.similarite(model,File)
    return render_template('s_resultats.html', File=File, resultat=round(resultat, 5))

@app.route('/a')
def a_accueil():
    """
    Cette fonction liste dans l'accueil les fichiers sur lesquels on peut effectuer les tests d'analogie

    :return: La liste des noms des fichiers sources pour les tests d'analogie
    """
    files = ["Questions Words (Google)"]
    return render_template('analogie.html', files=files)

@app.route('/a/resultat')
def a_resultat():
    """
    Cette fonction donne le résultat d'analogie pour les fichiers déjà chargés sur l'interface web

    :return: Le coefficent de corrélation correspondant au fichier sur lequel on clique sur l'interface web
    """
    File = request.args.get('file')
    if File == "Questions Words (Google)":
        accuracy = model.accuracy('../DATA/questions-words.txt')
        sum_corr = len(accuracy[-1]['correct'])
        sum_incorr = len((accuracy[-1]['incorrect']))
        total = sum_corr + sum_incorr
        percent = lambda a: a / total * 100
    else:
        #Ne rentre pas dans le ELSE, 1 seul fichier est disponible au traitement
        file="null"
        total="null"
        sum_corr="null"
        sum_incorr="null"
    return render_template('a_resultats.html', File=File, total=total, correct=round(percent(sum_corr),1), incorrect=round(percent(sum_incorr),1))

@app.errorhandler(404)
def ma_page_404(error):
    """
    Cette fonction permet de traiter l'erreur 404 lorsqu'une page n'est pas trouvée

    :return: Une page web erreur 404
    """
    return "Page non trouvée. Erreur ", 404

if __name__ == '__main__':s
    app.run(debug=True)
