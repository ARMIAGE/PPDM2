import gensim
import nltk
#nltk.download()
from nltk.corpus import brown
"""
sentences = brown.sents()
model = gensim.models.Word2Vec(sentences, min_count=1)
model.save("brown_model")
print ("Brown corpus model saved.")

model = gensim.models.Word2Vec.load("brown_model")
"""
print (model.wv.similarity('Sydney', 'koala'))