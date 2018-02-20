from gensim.models import word2vec
import file_insertion
import similarity
import fonctions_utiles

model = word2vec.Word2Vec.load('../MODEL/W2V_text8_Model.bin')

CSVFile = "../DATA/SimLex-999.txt"
data = file_insertion.insert_file_simlex999(CSVFile)

matrice = similarity.similarite(model, data)

print(matrice)
