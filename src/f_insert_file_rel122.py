def insert_file_rel122(chemin):
    mon_fichier = open(chemin, "r")
    global contenu
    contenu = mon_fichier.read()
    mon_fichier.close()
    contenu_ligne = contenu.split('\n')
    nb_lines = len(contenu_ligne) -1
    a = np.zeros(shape = (nb_lines,3))
    b = np.array(a,dtype=str)
    matrice = np.empty_like(b)
    
    laligne=0
    for ligne in contenu_ligne :
            if (ligne != ''):
                ligne_split = ligne.split("  ")
                ligne_split_split = ligne_split[1].split(" -- ")
                matrice[laligne,2]=ligne_split[0]
                matrice[laligne,0]=ligne_split_split[0]
                matrice[laligne,1]=ligne_split_split[1]
                x=float(matrice[laligne,2])
                x = x/4
                matrice[laligne,2]= str(x)
                laligne = laligne +1
    return matrice
