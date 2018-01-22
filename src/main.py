import file_insertion
import argparse
import fonctions_utiles
import text8

model = word2vec.Word2Vec.load('W2V_text8_Model.bin')

CSVFile = "../DATA/SimLex-999.txt"
data = file_insertion.insert_file_simlex999(CSVFile)

data = fonctions_utiles.liste_de_mots_contenus(model, data)
data = fonctions_utiles.extract_liste_de_mots(data)

print(data)
