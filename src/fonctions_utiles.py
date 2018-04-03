import operator
import numpy as np
import scipy


def tri_matrice(matrice):
    """
    Cette fonction a pour but de trier la matrice dans l'ordre alphabétique.
    :param matrice: matrice à trier
    :return: matrice triée dans l'ordre alphabétique sur les deux colonnes mots
    """
    return np.matrix(sorted(matrice, key=operator.itemgetter(2), reverse=True))


def calcul_similarite(model, liste_mots):
    """
    Cette fonction a pour but de calculer la similarité entre deux mots à partir d'un modèle précalculé
    :param model: modèle précalculé de wor2vec utilisant un corpus de mots provenant du Wikipedia anglais
    :param liste_mots: matrice trois colonnes dont les deux premières colonnes sont remplies par une liste de mot dont
     on veut calculer la similarité.
    :return:
    """
    a = np.zeros(shape=(len(liste_mots), 3))
    b = np.array(a, dtype=str)
    matrice = np.empty_like(b)
    i=0
    for ligne in liste_mots:
        matrice[(i, 0)] = ligne[0]
        matrice[(i, 1)] = ligne[1]
        matrice[(i, 2)] = (round(model.wv.similarity(ligne[0], ligne[1]),2))
        i = i + 1
    return matrice

    
# def calcul_similarite(model, liste_mots):
#     a = np.zeros(shape=(len(liste_mots),3))
#     b = np.array(a, dtype=str)
#     matrice = np.empty_like(b)
#     i=0
#     for ligne in liste_mots:
#         matrice[(i, 0)] = ligne[0]
#         matrice[(i, 1)] = ligne[1]
#         matrice[(i, 2)] = (round(model.wv.similarity(ligne[0], ligne[1]),2))
#         i = i +1
#     return matrice


def extract_liste_de_mots(matrice):
    """
    Fonction d'extraction de la liste de mot à partir d'une matrice de similarité
    :param matrice: matrice trois colonnes : mot1, mot2, similarité
    :return: liste de mots
    """
    return matrice[:, (0, 1)]

    
def est_dans_le_model(word_vectors, mot):
    """
    Fonction ayant pour but de savoir si le mot donné en entrée est présent dans le modèle.
    :param word_vectors: Vecteur contenant tout les mots du modèle
    :param mot: Mot à analyser
    :return: Vrai si le mot est dans le modèle et faux sinon
    """
    if mot not in word_vectors:
        return False
    else:
        return True


def liste_de_mots_contenus(model, data):
    word_vectors = model.wv
    l = 0
    for row in data:
        rep_mot1 = est_dans_le_model(word_vectors, row[0])
        rep_mot2 = est_dans_le_model(word_vectors, row[1])
        if(rep_mot1 is False or rep_mot2 is False):
            data = np.delete(data, (l), axis=0)
            l = l - 1
        l = l+1
    return data


def ajouter_colonne_rang(matrice):
    """
    Cette fonction permet de remplir la troisième colonne avec le rang du couple de mots
    :param matrice: matrice mot1, mot2 et troisième colonne vide.
    :return: matrice mot1, mot2, rang
    """
    i = 0
    rang = 1
    for ligne in matrice:
        matrice[i, 2] = rang
        i = i + 1
        rang = rang + 1
    return matrice


def tri_alphabetique(matrice):
    """
    Fonction de tri_alphabétique
    :param matrice: matrice à trier
    :return: matrice triée
    """
    a = np.array(matrice)
    return a[a[:, 0].argsort()]


def get_rang(matrice):
    """
    Fonbction permettant de récupérer le rang
    :param matrice: matrice mot1, mot2, rang
    :return: Colonne des rang
    """
    return matrice[:, 2]


def calcul_corellation(rang_humain, rang_word2vec):
    """
    Cette fonction permet de calculer la corrélation à partir des rangs
    :param rang_humain: rang provenant du modèle humain
    :param rang_word2vec: rang provenant du modèle informatique
    :return: Corrélation entre les deux rangs
    """
    tau, p_value = scipy.stats.kendalltau(rang_humain, rang_word2vec)
    return tau
