import file_insertion
import argparse
import fonctions_utiles
import text8
import similarity

model = word2vec.Word2Vec.load('W2V_text8_Model.bin')

CSVFile = "../DATA/SimLex-999.txt"
data = file_insertion.insert_file_simlex999(CSVFile)

#similarity.similarite(data)

def calcul_similarite(liste_mots):
    a = np.zeros(shape = (len(liste_mots),3))
    b = np.array(a,dtype=str)
    matrice = np.empty_like(b)
    i=0
    for ligne in liste_mots:
        matrice[(i,0)] = ligne[0]
        matrice[(i,1)] = ligne[1]
        matrice[(i,2)] = (round(model.wv.similarity(ligne[0], ligne[1]),2))
        i = i +1
    print(matrice)
    return matrice

matrice_clear = fonctions_utiles.liste_de_mots_contenus(model, data)
liste_mots = fonctions_utiles.extract_liste_de_mots(matrice_clear)
matrice = calcul_similarite(liste_mots)

