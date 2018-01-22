import file_insertion
import text8
import argparse
import fonctions_utiles

model = word2vec.Word2Vec.load('W2V_text8_Model.bin')
word_vectors = model.wv

CSVFile = "../DATA/SimLex-999.txt"

data = insert_file_simlex999(CSVFile)

def est_dans_le_model(mot):
    if mot not in word_vectors:
        return False
    else :
        return True

def liste_de_mots_contenus(data):
    l=0
    for row in data:
        rep_mot1 = est_dans_le_model(row[0])
        rep_mot2 = est_dans_le_model(row[1])
        if(rep_mot1 is False and rep_mot1 is False):
            data = np.delete(data, (l), axis=0)
            l = l - 1
    l = l+1
    return data

data=liste_de_mots_contenus(data)
data = fonctions_utiles.extract_liste_de_mots(data)
print(data)
