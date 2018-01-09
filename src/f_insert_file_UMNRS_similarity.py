def insert_file_UMNRS_similarity(chemin):
    mon_fichier = open(chemin, "r")
    global contenu
    contenu = mon_fichier.read()
    mon_fichier.close()
    contenu_ligne = contenu.split('\n')
    del contenu_ligne[0]
    nb_lines = len(contenu_ligne) -1
    a = np.zeros(shape = (nb_lines,3))
    b = np.array(a,dtype=str)
    matrice = np.empty_like(b)
    
    laligne=0
    for ligne in contenu_ligne :
            if (ligne != ''):
                matrice[laligne,0]=(ligne.split(","))[2]
                matrice[laligne,1]=(ligne.split(","))[3]
                matrice[laligne,2]=(ligne.split(","))[0]
                x=float(matrice[laligne,2])
                x = x/1600
                matrice[laligne,2]= str(x)
                laligne = laligne +1
    return matrice
    
