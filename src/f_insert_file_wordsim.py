def insert_file_wordsim(chemin):
    mon_fichier = open(chemin, "r")
    global contenu
    contenu = mon_fichier.read()
    mon_fichier.close()
    contenu_ligne = contenu.split('\n')
    nb_lines = len(contenu_ligne) -2
    a = np.zeros(shape = (nb_lines,3))
    b = np.array(a,dtype=str)
    matrice = np.empty_like(b)
    
    laligne=0
    for ligne in contenu_ligne :
            if (ligne != ''):
                matrice[laligne,0]=(ligne.split(";"))[0]
                matrice[laligne,1]=(ligne.split(";"))[1]
                matrice[laligne,2]=(ligne.split(";"))[2]
                x=float(matrice[laligne,2])
                x = x/10
                matrice[laligne,2]= str(x)
                laligne = laligne +1
    return matrice