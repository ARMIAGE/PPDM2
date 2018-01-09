import operator

def tri_matrice(matrice):
    return np.matrix(sorted(matrice, key=operator.itemgetter(2), reverse=True))

def extract_liste_de_mots(matrice):
    return matrice[:,(0,1)]

def calcul_similarite(liste_mots):
    return matrice_word2vec
    
def ajouter_colonne_rang(matrice):
    i = 0
    rang = 1
    for ligne in matrice :
        matrice[i,2] = rang
        i = i + 1
        rang = rang + 1
    return matrice 