import operator

def tri_matrice(matrice):
    return np.matrix(sorted(matrice, key=operator.itemgetter(2), reverse=True))

def extract_liste_de_mots(matrice):
    return matrice[:,(0,1)]

def calcul_similarite(liste_mots):
    return matrice_word2vec