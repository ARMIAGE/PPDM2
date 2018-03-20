import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import word2vec
import file_insertion
import similarity
import warnings
import argparse

#Similarity arguments
parser = argparse.ArgumentParser()
parser.add_argument("--rg", help="Similarity test for rg file", action="store_true")
parser.add_argument("--cos_matrix", help="Similarity test for cos matrix brm IFR file", action="store_true")
parser.add_argument("--mturk", help="Similary test for mturk 771 file", action="store_true")
parser.add_argument("--mc", help="Similarity test for mc file", action="store_true")
parser.add_argument("--rel", help="Similarity test for rel122 norms file", action="store_true")
parser.add_argument("--simlex", help="Similarity test for simlex 999 file", action="store_true")
parser.add_argument("--umnsrs", help="Similarity test for umnsrs file", action="store_true")
parser.add_argument("--wordsim", help="Similarity test for wordsim file", action="store_true")
args = parser.parse_args()

warnings.filterwarnings('ignore', '.*nan.*',)

model = word2vec.Word2Vec.load('../MODEL/W2V_text8_Model.bin')


print("Le coefficient de qualité du fichier (%)")

if args.rg:
    print(similarity.similarite(model, file_insertion.insert_file_rg()))
elif args.cos_matrix:
    print(similarity.similarite(model, file_insertion.insert_file_cos_matrix_brm_ifr()))
elif args.mturk:
    print(similarity.similarite(model, file_insertion.insert_file_mturk771()))
elif args.mc:
    print(similarity.similarite(model, file_insertion.insert_file_mc()))
elif args.rel:
    print(similarity.similarite(model, file_insertion.insert_file_rel122()))
elif args.simlex:
    print(similarity.similarite(model, file_insertion.insert_file_simlex999()))
elif args.umnsrs:
    print(similarity.similarite(model, file_insertion.insert_file_UMNRS_similarity()))
elif args.wordsim:
    print(similarity.similarite(model, file_insertion.insert_file_wordsim()))

#ANALOGIE
#accuracy = model.accuracy('../DATA/questions-words.txt')
#sum_corr = len(accuracy[-1]['correct'])
#sum_incorr = len((accuracy[-1]['incorrect'])
#total = sum_corr + sum_incorr
#percent = lambda a: a / total * 100
#print(accuracy[-1]['correct'])
#print((accuracy[-1]['incorrect'])
#print('Nombre de phrases: {}, Correctes: {:.2f}%, Incorrectes: {:.2f}%'.format(total, percent(sum_corr), percent(sum_incorr)))