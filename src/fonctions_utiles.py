import operator
import numpy as np
import scipy

def tri_matrice(matrice):
    return np.matrix(sorted(matrice, key=operator.itemgetter(2), reverse=True))


def extract_liste_de_mots(matrice):
    return matrice[:, (0, 1)]
    
def est_dans_le_model(word_vectors, mot):
    if mot not in word_vectors:
        return False
    else :
        return True    

def liste_de_mots_contenus(model, data):
    word_vectors = model.wv
    l=0
    for row in data:
        rep_mot1 = est_dans_le_model(word_vectors, row[0])
        rep_mot2 = est_dans_le_model(word_vectors, row[1])
        if(rep_mot1 is False or rep_mot2 is False):
            data = np.delete(data, (l), axis=0)
            l = l - 1
        l = l+1
    return data

def calcul_similarite(liste_mots):
    matrice_word2vec=liste_mots
    return matrice_word2vec


def ajouter_colonne_rang(matrice):
    i = 0
    rang = 1
    for ligne in matrice:
        matrice[i, 2] = rang
        i = i + 1
        rang = rang + 1
    return matrice


def tri_alphabetique(matrice):
    return np.matrix(sorted(matrice, key=operator.itemgetter(0, 1)))


def get_rang(matrice):
    return matrice[:, 2]


def calcul_corellation(rang_humain, rang_word2vec):
    tau, p_value = scipy.stats.kendalltau(rang_humain, rang_word2vec)
    return tau
