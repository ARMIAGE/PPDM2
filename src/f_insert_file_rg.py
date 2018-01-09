def insert_file_rg(path):
    mon_fichier = open(path, "r")
    content = mon_fichier.read()
    mon_fichier.close()

    # splitter par ligne pour créer une liste
    content_line = content.split("\n")

    # remplacer les tabulations par des virgules dans la liste (entre chaque mot) quand nécessaire
    # content_line = [cl.replace('\t',',') for cl in content_line]
    # print(content_line)

    # init matrice de taille nb_lignes du fichier, nb_colonnes = 3
    nb_lines = len(content_line) - 1

    a = np.zeros(shape=(nb_lines, 3))

    b = np.array(a, dtype=str)

    matrice = np.empty_like(b)
    # print(matrice)

    laligne = 0
    for ligne in content_line:
        if ligne != '':
            ligne_split = ligne.split(";")
            matrice[laligne, 0] = ligne_split[0]
            matrice[laligne, 1] = ligne_split[1]
            matrice[laligne, 2] = ligne_split[2]
            x = float(matrice[laligne, 2])
            x = x / 4
            matrice[laligne, 2] = str(x)

            laligne = laligne + 1

    return matrice
