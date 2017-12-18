import csv
import numpy as np

i = 0

with open("C:/Users/Alexa/Desktop/PPD/PROJET/DATA/SimLex-999.txt") as f:
    reader = csv.reader(f, dialect='excel', delimiter='\t')
    for row in reader:
        if i == 0:
            entete = np.matrix([row])
            i = i + 1
        else:
            newrow = np.matrix([row])
            data = np.append(data, newrow, axis=0)

            
            
print("-------")
print(data[0,0])
print(data[0,1])
print(data[0,3])
print("-------")
