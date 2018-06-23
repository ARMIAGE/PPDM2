import operator
import numpy as np
import scipy
from gensim.models import word2vec

import file_insertion


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
    """
        Fonction permettant de nettoyer la matrice de base des mots non contenus dans le model.

        :param model: Modèle de word embedings
        :param data: Données en entrée à traiter
        :return: Matrice de mot nettoyée

        >>> liste_de_mots_contenus(word2vec.Word2Vec.load('MODEL/W2V_text8_Model.bin'), file_insertion.insert_file_generic("../DATA/matrice_test.csv"))
        array([['love', 'sex', '6.77'],
               ['tiger', 'cat', '7.35']], dtype='<U32')


        """
    #word_vectors = model.wv
    word_vectors = model
    l = 0
    for row in data:
        rep_mot1 = est_dans_le_model(word_vectors, row[0])
        rep_mot2 = est_dans_le_model(word_vectors, row[1])
        if(rep_mot1 is False or rep_mot2 is False):
            data = np.delete(data, (l), axis=0)
            l = l - 1
        l = l+1
    return data


def extract_liste_de_mots(matrice):
    """
    Fonction d'extraction de la liste de mot à partir d'une matrice de similarité

    :param matrice: matrice trois colonnes : mot1, mot2, similarité
    :return: liste de mots

    >>> extract_liste_de_mots(liste_de_mots_contenus(word2vec.Word2Vec.load('MODEL/W2V_text8_Model.bin'), file_insertion.insert_file_generic("../DATA/matrice_test.csv")))
    array([['love', 'sex'],
           ['tiger', 'cat']], dtype='<U32')

    """
    return matrice[:, (0, 1)]


def tri_matrice(matrice):
    """
    Cette fonction a pour but de trier la matrice par ordre de similiarité décroissant.

    :param matrice: matrice à trier
    :return: matrice triée

    >>> tri_matrice(file_insertion.insert_file_generic("../DATA/matrice_test.csv"))
    matrix([['tiger', 'cat', '7.35'],
            ['love', 'sex', '6.77']], dtype='<U32')

    """
    return np.matrix(sorted(matrice, key=operator.itemgetter(2), reverse=True))


def calcul_similarite(model, liste_mots):
    """
    Cette fonction a pour but de calculer la similarité entre deux mots à partir d'un modèle précalculé

    :param model: modèle précalculé de wor2vec utilisant un corpus de mots provenant du Wikipedia anglais
    :param liste_mots: matrice trois colonnes dont les deux premières colonnes sont remplies par une liste de mot dont on veut calculer la similarité.
    :return: matrice 3 colonnes avec nos deux mots et la similarité calculée

    >>> calcul_similarite(word2vec.Word2Vec.load('MODEL/W2V_text8_Model.bin'),extract_liste_de_mots(liste_de_mots_contenus(word2vec.Word2Vec.load('MODEL/W2V_text8_Model.bin'), file_insertion.insert_file_generic("../DATA/matrice_test.csv"))))
    array([['love', 'sex', '0.41'],
           ['tiger', 'cat', '0.55']], dtype='<U32')

    """
    a = np.zeros(shape=(len(liste_mots), 3))
    b = np.array(a, dtype=str)
    matrice = np.empty_like(b)
    i=0
    for ligne in liste_mots:
        matrice[(i, 0)] = ligne[0]
        matrice[(i, 1)] = ligne[1]
        #matrice[(i, 2)] = (round(model.wv.similarity(ligne[0], ligne[1]),2))
        matrice[(i, 2)] = (round(model.similarity(ligne[0], ligne[1]), 2))
    return matrice


def ajouter_colonne_rang(matrice):
    """
    Cette fonction permet de remplir la troisième colonne avec le rang du couple de mots

    :param matrice: matrice mot1, mot2 et troisième colonne vide.
    :return: matrice mot1, mot2, rang

    >>> ajouter_colonne_rang(tri_matrice(file_insertion.insert_file_generic("../DATA/matrice_test.csv")))
    matrix([['tiger', 'cat', '1'],
            ['love', 'sex', '2']], dtype='<U32')

    >>> ajouter_colonne_rang(tri_matrice(calcul_similarite(word2vec.Word2Vec.load('MODEL/W2V_text8_Model.bin'),extract_liste_de_mots(liste_de_mots_contenus(word2vec.Word2Vec.load('MODEL/W2V_text8_Model.bin'), file_insertion.insert_file_generic("../DATA/matrice_test.csv"))))))
    matrix([['tiger', 'cat', '1'],
            ['love', 'sex', '2']], dtype='<U32')
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

    >>> tri_alphabetique(ajouter_colonne_rang(tri_matrice(file_insertion.insert_file_generic("../DATA/matrice_test.csv"))))
    array([['love', 'sex', '2'],
           ['tiger', 'cat', '1']], dtype='<U32')
    """
    a = np.array(matrice)
    return a[a[:, 0].argsort()]


def get_rang(matrice):
    """
    Fonction permettant de récupérer le rang

    :param matrice: matrice mot1, mot2, rang
    :return: Colonne des rang

    >>> get_rang(ajouter_colonne_rang(tri_matrice(file_insertion.insert_file_generic("../DATA/matrice_test.csv"))))
    matrix([['1'],
            ['2']], dtype='<U32')
    """
    return matrice[:, 2]


def calcul_corellation(rang_humain, rang_word2vec):
    """
    Cette fonction permet de calculer la corrélation à partir des rangs

    :param rang_humain: rang provenant du modèle humain
    :param rang_word2vec: rang provenant du modèle informatique
    :return: Corrélation entre les deux rangs

    >>> calcul_corellation(get_rang(tri_alphabetique(ajouter_colonne_rang(tri_matrice(file_insertion.insert_file_generic("../DATA/matrice_test.csv"))))),get_rang(tri_alphabetique(ajouter_colonne_rang(tri_matrice(calcul_similarite(word2vec.Word2Vec.load('MODEL/W2V_text8_Model.bin'),extract_liste_de_mots(liste_de_mots_contenus(word2vec.Word2Vec.load('MODEL/W2V_text8_Model.bin'), file_insertion.insert_file_generic("../DATA/matrice_test.csv")))))))))
    1.0

    """
    tau, p_value = scipy.stats.kendalltau(rang_humain, rang_word2vec)
    return tau


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












