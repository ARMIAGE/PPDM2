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
    return dict(titre="Word Embedding Application")

@app.route('/')
def accueil():
    typeFichier = ["Cos Matrix BRM IFR", "MC", "MTURK-771", "rel122-norms", "RG", "SimLex-999", "WordSim"]
    return render_template('accueil.html', typeFichier=typeFichier)

@app.route("/s_upload", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    return render_template('s_upload.html')

@app.route('/resultat')
def resultat():
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
        File = "Not Found"
    return render_template('similarite_resultats.html', File=File, resultat=resultat)

@app.errorhandler(404)
def ma_page_404(error):
    return "Page non trouvée. Erreur ", 404


if __name__ == '__main__':
    app.run(debug=True)
