from gensim.models import word2vec
import file_insertion
import similarity
import fonctions_utiles
import warnings

warnings.filterwarnings('ignore', '.*nan.*',)

model = word2vec.Word2Vec.load('../MODEL/W2V_text8_Model.bin')

#SIMILARITE
data = file_insertion.insert_file_rg()
coef = similarity.similarite(model, data)
print("Le coefficient de qualité du fichier (%)")
print(coef)

#ANALOGIE
accuracy = model.accuracy('../DATA/questions-words.txt')
sum_corr = len(accuracy[-1]['correct'])
sum_incorr = len(accuracy[-1]['incorrect'])
total = sum_corr + sum_incorr
percent = lambda a: a / total * 100
print('Nombre de phrases: {}, Correctes: {:.2f}%, Incorrectes: {:.2f}%'.format(total, percent(sum_corr), percent(sum_incorr)))