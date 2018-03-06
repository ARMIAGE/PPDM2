from gensim.models import word2vec
import file_insertion
import similarity
import fonctions_utiles
import warnings

warnings.filterwarnings('ignore', '.*nan.*',)

    
model = word2vec.Word2Vec.load('../MODEL/W2V_text8_Model.bin')

file = "../DATA/SimLex-999.txt"
data = file_insertion.insert_file_simlex999(file)

coef = similarity.similarite(model, data)
coef = round(coef*100)
print("Le coefficient de qualité du fichier (%)")
print(coef)
