import os
os.chdir("C:/Users/Alexa/Desktop/PPD/PROJET/PPDM2/src")
from f_insert_file_simlex999 import insert_file_simlex999
from f_insert_file_rel122 import insert_file_rel122
from f_insert_file_mturk771 import insert_file_mturk771

CSVFile = "C:/Users/Alexa/Desktop/PPD/PROJET/DATA/SimLex-999.txt"

data = insert_file_simlex999(CSVFile)
print("-------")
print(data)
print("-------")
