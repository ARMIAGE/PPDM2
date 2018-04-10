import fonctions_utiles

def similarite(model, matrice):
    """
        Cette fonction réalise l'enchaînement des fonctions permettant d'obtenir le coefficent de similarité d'un modèle de données
        :param model: modèle de données text8 récupéré à partir de wikipedia anglais
        :param matrice: jeu de données analysé, rendu sous forme de matrice
        :return: Retourne le coefficent de similarité entre le modèle text8 et le jeu de données sous forme de matrice fourni en entrée
    """
    #Verification de l'existence des mots dans le model
    matrice_clear = fonctions_utiles.liste_de_mots_contenus(model, matrice)

    
    # Extraction de la liste des mots (mot1, mot2)
    liste_mots = fonctions_utiles.extract_liste_de_mots(matrice_clear)

    # Creation matrice W2V (mot1, mot2, coef)
    matrice_word2vec = fonctions_utiles.calcul_similarite(model, liste_mots)
    
    # Tri par ordre de similarite
    matrice = fonctions_utiles.tri_matrice(matrice_clear)
    matrice_word2vec = fonctions_utiles.tri_matrice(matrice_word2vec)

    # Ajout du rang
    matrice = fonctions_utiles.ajouter_colonne_rang(matrice)
    matrice_word2vec = fonctions_utiles.ajouter_colonne_rang(matrice_word2vec)

    # Tri Alphabetique pour comparaison finale
    matrice = fonctions_utiles.tri_alphabetique(matrice)
    matrice_word2vec = fonctions_utiles.tri_alphabetique(matrice_word2vec)

    # Recuperation du rang
    rang_humain = fonctions_utiles.get_rang(matrice)
    rang_word2vec = fonctions_utiles.get_rang(matrice_word2vec)

    # Qualité du fichier compare
    coef_similarite = fonctions_utiles.calcul_corellation(rang_humain, rang_word2vec)
    return coef_similarite
