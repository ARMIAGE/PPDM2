def similarite (matrice)
    liste_mots = extract_liste_de_mots(matrice)
    matrice_word2vec = calcul_similarite(liste_mots)
    matrice_humain_triee = tri_matrice(matrice)
    matrice_word2vec_triee = tri_matrice(matrice_word2vec)
    coef_similarite = calcul_corellation(matrice_humain_triee, matrice_word2vec_triee)
return coef_similarite