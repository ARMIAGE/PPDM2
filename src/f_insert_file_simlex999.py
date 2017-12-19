import csv
import numpy as np

def insert_file_simlex999(CSVFile):
    global data
    
    i = 0

    with open(CSVFile) as f:
        reader = csv.reader(f, dialect='excel', delimiter="\t")
        for row in reader:
            if i == 0:
                data = np.matrix([row])
                i = i + 1
            else:
                data = np.append(data, np.matrix([row]), axis=0)
    return data[:, [0, 1, 3]]