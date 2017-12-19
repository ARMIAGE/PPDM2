import numpy as np 
def insert_file_mturk771(path):
    file = open(path,"r")
    content = file.read()
    file.close()
    content_line = content.split("\n")
    nb_lines =len(content_line)-1
    a = np.zeros(shape = (nb_lines,3))
    b = np.array(a,dtype=str)
    matrice = np.empty_like(b)
    laligne = 0
    for ligne in content_line:
            if (ligne != ''):
                matrice[laligne,0] = (ligne.split(','))[0]
                matrice[laligne,1] = (ligne.split(','))[1]
                matrice[laligne,2] = (ligne.split(','))[2]
                x = float(matrice[laligne,2])
                x = x/5
                matrice[laligne,2] = str(x)
                laligne = laligne + 1
    return (matrice)