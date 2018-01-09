import csv
import numpy as np
CSVFile = "C:/Users/Alexa/Desktop/PPD/PROJET/DATA/SimLex-999.txt"
def insert_file_simlex999(CSVFile):
    mon_fichier = open(CSVFile, "r")
    global contenu
    contenu = mon_fichier.read()
    mon_fichier.close()
    contenu_ligne = contenu.split('\n')
    nb_lines = len(contenu_ligne) -1
    a = np.zeros(shape = (nb_lines,3))
    b = np.array(a,dtype=str)
    matrice = np.empty_like(b)

    del contenu_ligne [0]

    laligne=0
    for ligne in contenu_ligne :
        if (ligne != ''):
            ligne_split = ligne.split("\t")
            matrice[laligne,0]=ligne_split[0]
            matrice[laligne,1]=ligne_split[1]
            matrice[laligne,2]=ligne_split[3]
            x=float(matrice[laligne,2])
            x = x/10
            matrice[laligne,2]= str(x)
            laligne = laligne +1
    return matrice