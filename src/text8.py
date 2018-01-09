from gensim.models import word2vec
import logging
import warnings

def initModel():
    warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    
    sentences = word2vec.Text8Corpus("C:/Users/Alexa/Desktop/PPD/text8")
    
    model = word2vec.Word2Vec(sentences, size=200)
    return model