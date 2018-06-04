import logging
import warnings
from gensim.models import word2vec

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def initModel():
    """
    Cette fonction permet d'initialiser le modèle text8 et de persister le modèle sur le disque dans un fichier .bin
s
    :return: Retourne le modèle de données text8
    """
    sentences = word2vec.Text8Corpus("../DATA/text8")
    model = word2vec.Word2Vec(sentences, size=200)
    model.save('../MODEL//W2V_text8_Model.bin')
    return model

#initModel()

