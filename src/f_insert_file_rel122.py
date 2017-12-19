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
                matrice[laligne,2]=(ligne.split("  "))[0]
                matrice[laligne,0]=(ligne.split("  "))[1].split(" -- ")[0]
                matrice[laligne,1]=(ligne.split("  "))[1].split(" -- ")[1]
                x=float(matrice[laligne,2])
                x = x/4
                matrice[laligne,2]= str(x)
                laligne = laligne +1
    return matrice
