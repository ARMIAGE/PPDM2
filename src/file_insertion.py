import pandas as pd
import numpy as np
import xlrd
import csv


def insert_file_cos_matrix_brm_ifr(path):
    # recuperation des donnees de chaque onglet
    first_sheet = pd.read_excel(path, sheetname='1st_200')
    second_sheet = pd.read_excel(path, sheetname='2nd_200')
    third_sheet = pd.read_excel(path, sheetname='last_141')

    # depivotage des donnees de chaque onglet du fichier excel pour avoir la structure : mot 1, mot 2, correlation
    unpivot_first_sheet = pd.melt(first_sheet, id_vars=['CONCEPT'], var_name="mot 2", value_name="correlation")
    unpivot_second_sheet = pd.melt(second_sheet, id_vars=['CONCEPT'], var_name="mot 2", value_name="correlation")
    unpivot_third_sheet = pd.melt(third_sheet, id_vars=['CONCEPT'], var_name="mot 2", value_name="correlation")

    # concat des 3 listes
    dataframe = pd.concat([unpivot_first_sheet, unpivot_second_sheet, unpivot_third_sheet])

    matrix = dataframe.as_matrix()

    return matrix


def insert_file_mc(chemin):
    mon_fichier = open(chemin, "r")
    global contenu
    contenu = mon_fichier.read()
    mon_fichier.close()
    contenu_ligne = contenu.split('\n')
    nb_lines = len(contenu_ligne) - 2
    a = np.zeros(shape=(nb_lines, 3))
    b = np.array(a, dtype=str)
    matrice = np.empty_like(b)

    laligne = 0
    for ligne in contenu_ligne:
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


def insert_file_mturk771(path):
    mon_fichier = open(path, "r")
    content = mon_fichier.read()
    mon_fichier.close()
    content_line = content.split("\n")
    nb_lines = len(content_line) - 1
    a = np.zeros(shape=(nb_lines, 3))
    b = np.array(a, dtype=str)
    matrice = np.empty_like(b)
    laligne = 0
    for ligne in content_line:
        if ligne != '':
            ligne_split = ligne.split(",")
            matrice[laligne, 0] = ligne_split[0]
            matrice[laligne, 1] = ligne_split[1]
            matrice[laligne, 2] = ligne_split[2]
            x = float(matrice[laligne, 2])
            x = x / 5
            matrice[laligne, 2] = str(x)
            laligne = laligne + 1
    return matrice


def insert_file_rel122(chemin):
    mon_fichier = open(chemin, "r")
    global contenu
    contenu = mon_fichier.read()
    mon_fichier.close()
    contenu_ligne = contenu.split('\n')
    nb_lines = len(contenu_ligne) - 1
    a = np.zeros(shape=(nb_lines, 3))
    b = np.array(a, dtype=str)
    matrice = np.empty_like(b)

    laligne = 0
    for ligne in contenu_ligne:
        if ligne != '':
            ligne_split = ligne.split("  ")
            ligne_split_split = ligne_split[1].split(" -- ")
            matrice[laligne, 2] = ligne_split[0]
            matrice[laligne, 0] = ligne_split_split[0]
            matrice[laligne, 1] = ligne_split_split[1]
            x = float(matrice[laligne, 2])
            x = x / 4
            matrice[laligne, 2] = str(x)
            laligne = laligne + 1
    return matrice


def insert_file_rg(path):
    mon_fichier = open(path, "r")
    content = mon_fichier.read()
    mon_fichier.close()

    # splitter par ligne pour creer une liste
    content_line = content.split("\n")

    # remplacer les tabulations par des virgules dans la liste (entre chaque mot) quand necessaire
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


def insert_file_simlex999(CSVFile):
    mon_fichier = open(CSVFile, "r")
    global contenu
    contenu = mon_fichier.read()
    mon_fichier.close()
    contenu_ligne = contenu.split('\n')
    nb_lines = len(contenu_ligne) - 1
    a = np.zeros(shape=(nb_lines, 3))
    b = np.array(a, dtype=str)
    matrice = np.empty_like(b)

    del contenu_ligne[0]

    laligne = 0
    for ligne in contenu_ligne:
        if ligne != '':
            ligne_split = ligne.split("\t")
            matrice[laligne, 0] = ligne_split[0]
            matrice[laligne, 1] = ligne_split[1]
            matrice[laligne, 2] = ligne_split[3]
            x = float(matrice[laligne, 2])
            x = x / 10
            matrice[laligne, 2] = str(x)
            laligne = laligne + 1
    return matrice


def insert_file_UMNRS_similarity(chemin):
    mon_fichier = open(chemin, "r")
    global contenu
    contenu = mon_fichier.read()
    mon_fichier.close()
    contenu_ligne = contenu.split('\n')
    del contenu_ligne[0]
    nb_lines = len(contenu_ligne) - 1
    a = np.zeros(shape=(nb_lines, 3))
    b = np.array(a, dtype=str)
    matrice = np.empty_like(b)

    laligne = 0
    for ligne in contenu_ligne:
        if ligne != '':
            ligne_split = ligne.split(",")
            matrice[laligne, 0] = ligne_split[2]
            matrice[laligne, 1] = ligne_split[3]
            matrice[laligne, 2] = ligne_split[0]
            x = float(matrice[laligne, 2])
            x = x / 1600
            matrice[laligne, 2] = str(x)
            laligne = laligne + 1
    return matrice


def insert_file_wordsim(chemin):
    mon_fichier = open(chemin, "r")
    global contenu
    contenu = mon_fichier.read()
    mon_fichier.close()
    contenu_ligne = contenu.split('\n')
    nb_lines = len(contenu_ligne) - 2
    a = np.zeros(shape=(nb_lines, 3))
    b = np.array(a, dtype=str)
    matrice = np.empty_like(b)

    laligne = 0
    for ligne in contenu_ligne:
        if ligne != '':
            ligne_split = ligne.split(";")
            matrice[laligne, 0] = ligne_split[0]
            matrice[laligne, 1] = ligne_split[1]
            matrice[laligne, 2] = ligne_split[2]
            x = float(matrice[laligne, 2])
            x = x / 10
            matrice[laligne, 2] = str(x)
            laligne = laligne + 1
    return matrice