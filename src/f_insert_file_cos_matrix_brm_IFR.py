import pandas as pd
import xlrd


def insert_file_cos_matrix_brm_IFR(path):

    # récupération des données de chaque onglet
    first_sheet = pd.read_excel(path,sheetname='1st_200')
    second_sheet = pd.read_excel(path,sheetname='2nd_200')
    third_sheet = pd.read_excel(path,sheetname='last_141')
    
    # dépivotage des données de chaque onglet du fichier excel pour avoir la structure : mot 1, mot 2, corrélation
    unpivot_first_sheet = pd.melt(first_sheet, id_vars=['CONCEPT'], var_name="mot 2", value_name="correlation")
    unpivot_second_sheet = pd.melt(second_sheet, id_vars=['CONCEPT'], var_name="mot 2", value_name="correlation")
    unpivot_third_sheet = pd.melt(third_sheet, id_vars=['CONCEPT'], var_name="mot 2", value_name="correlation")
    
    # concat des 3 listes 
    dataframe = pd.concat([unpivot_first_sheet, unpivot_second_sheet, unpivot_third_sheet])
    
    matrix = dataframe.as_matrix()
    
    return (matrix)

f_insert_file_rg(r'''C:\Users\alexv\Documents\MIAGE\MASTER\Master2\PPD\Dataset\cos_matrix_brm_IFR.xlsx''')
