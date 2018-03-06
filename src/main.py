from gensim.models import word2vec
import file_insertion
import similarity
import warnings

warnings.filterwarnings('ignore', '.*nan.*',)

model = word2vec.Word2Vec.load('../MODEL/W2V_text8_Model.bin')
data = file_insertion.insert_file_rg()
coef = similarity.similarite(model, data)
print("Le coefficient de qualité du fichier (%)")
print(coef)
