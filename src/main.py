from f_insert_file_simlex999 import insert_file_simlex999
from f_insert_file_rel122 import insert_file_rel122
from f_insert_file_mturk771 import insert_file_mturk771
from f_insert_file_mc import insert_file_mc
from f_insert_file_wordsim import insert_file_wordsim
from f_insert_file_rg import insert_file_rg
from f_insert_file_UMNRS_similarity import insert_file_UMNRS_similarity
import text8

#initModel()

CSVFile = "../DATA/SimLex-999.txt"

data = insert_file_simlex999(CSVFile)
print("-------")
word1 = data[1,0];
word2 = data[1,1];
print("Word 1 : " + word1 + " - Word 2 : " + word2)

print("-------")

print("SimLex999 estimation : ")
CoeffSimLex = round(float(data[1,2])/10,2)
print(CoeffSimLex)

print("-------")

print("Gensim Word2Vec Text8 estimation : ")
Coeffword2vec=round(text8.model.wv.similarity(word1, word2),2)
print(Coeffword2vec)

print("-------")



