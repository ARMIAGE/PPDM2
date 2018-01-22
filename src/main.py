import file_insertion
import text8
import argparse
import fonctions_utiles

model = word2vec.Word2Vec.load('W2V_text8_Model.bin')

CSVFile = "../DATA/SimLex-999.txt"

data = insert_file_simlex999(CSVFile)

# word1 = data[1,0];
# word2 = data[1,1];
# print("Word 1 : " + word1 + " - Word 2 : " + word2)

# print("SimLex999 estimation : ")
# CoeffSimLex = round(float(data[1,2])/10,2)
# print(CoeffSimLex)

# print("Gensim Word2Vec Text8 estimation : ")
# Coeffword2vec=round(model.wv.similarity(word1, word2),2)
# print(Coeffword2vec)

# print(data[:, (0, 1)])
# print(round(model.wv.similarity(word1, word2), 2))

#print(data)

#fonctions_utiles.tri_alphabetique(data)

# calcul_similarite

print(data[:,(0,1)])
print(round(model.wv.similarity(word1, word2),2))
print(len(data))
data=(data[:,(0,1)])

a = np.zeros(shape = (len(data),3))
b = np.array(a,dtype=str)
matrice = np.empty_like(b)
l=0
NotIn = 0
ListeNotIn = []
word_vectors = model.wv

for row in data:
    if (row[0] in word_vectors and row[1] in word_vectors.vocab):
        matrice[l,0]=row[0]
        matrice[l,1]=row[1]
        matrice[l,2]=round(model.wv.similarity(row[0], row[1]),2)
    else :
        NotIn = NotIn +1
        data = np.delete(data, l)
    if row[0] not in word_vectors:
        ListeNotIn.append(row[0])
    if row[1] not in word_vectors:
        ListeNotIn.append(row[1])
    l = l+1

long=len(matrice)-len(ListeNotIn)
#print(matrice[:(long)])


print(data[500,])
M = np.delete(data, (500), axis=0)
print(M[500,])