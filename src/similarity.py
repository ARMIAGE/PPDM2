import fonctions_utiles


def similarite(matrice):
    # Extraction de la liste des mots (mot1, mot2)
    liste_mots = fonctions_utiles.extract_liste_de_mots(matrice)

    # Creation matrice W2V (mot1, mot2, coef)
    matrice_word2vec = calcul_similarite(liste_mots)

    # Tri par ordre de similarite
    matrice = fonctions_utiles.tri_matrice(matrice)
    matrice_word2vec = fonctions_utiles.tri_matrice(matrice_word2vec)

    # Ajout du rang
    matrice = fonctions_utiles.ajouter_colonne_rang(matrice)
    matrice_word2vec = fonctions_utiles.ajouter_colonne_rang(matrice_word2vec)

    # Tri Alphabetique pour comparaison finale
    matrice = tri_alphabetique(matrice)
    matrice_word2vec = tri_alphabetique(matrice_word2vec)

    # Recuperation du rang
    rang_humain = get_rang(matrice)
    rang_word2vec = get_rang(matrice_word2vec)

    # Qualité du fichier compare
    coef_similarite = calcul_corellation(rang_humain, rang_word2vec)
    return coef_similarite
