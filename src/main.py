import file_insertion
import argparse
import fonctions_utiles
import text8s
import similarity

"""
model = word2vec.Word2Vec.load('W2V_text8_Model.bin')

CSVFile = "../DATA/SimLex-999.txt"
data = file_insertion.insert_file_simlex999(CSVFile)

#similarity.similarite(data)

matrice_clear = fonctions_utiles.liste_de_mots_contenus(model, data)
liste_mots = fonctions_utiles.extract_liste_de_mots(matrice_clear)


#calcul_similarite
a = np.zeros(shape = (len(liste_mots),3))
b = np.array(a,dtype=str)
matrice = np.empty_like(b)
print(matrice)

i=0
for ligne in matrice_clear:        
    print(round(model.wv.similarity(ligne[0], ligne[1]),2))
    #CREER LA MATRICE W2V MOT1, MOT2, VALEUR

print(liste_mots[0,1])
print(liste_mots[1,1]) """



print(file_insertion.insert_file_cos_matrix_brm_ifr())