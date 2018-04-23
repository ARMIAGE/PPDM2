import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import word2vec
import file_insertion
import similarity
import warnings
import argparse
import analogie

#Similarity arguments
parser = argparse.ArgumentParser()
parser.add_argument("--rg", help="Similarity test for rg file", action="store_true")
parser.add_argument("--cos_matrix", help="Similarity test for cos matrix brm IFR file", action="store_true")
parser.add_argument("--mturk", help="Similary test for mturk 771 file", action="store_true")
parser.add_argument("--mc", help="Similarity test for mc file", action="store_true")
parser.add_argument("--rel", help="Similarity test for rel122 norms file", action="store_true")
parser.add_argument("--simlex", help="Similarity test for simlex 999 file", action="store_true")
# parser.add_argument("--umnrs", help="Similarity test for umnsrs file", action="store_true")
parser.add_argument("--wordsim", help="Similarity test for wordsim file", action="store_true")

parser.add_argument("--analogie", help="Analogie with Questions Words (Google) on Text8 Model", action="store_true")

args = parser.parse_args()

warnings.filterwarnings('ignore', '.*nan.*',)

try:
    model = word2vec.Word2Vec.load('../MODEL/W2V_text8_Model.bin')
except:
    print("Erreur lors de la récupération du Model TEXT8")

print("Calcul du coefficient de qualité du fichier...")

if args.rg:
    try:
        print(similarity.similarite(model, file_insertion.insert_file_rg()))
    except:
        print("Erreur lors de l'execution du script de similarité")
elif args.cos_matrix:
    try:
        print(similarity.similarite(model, file_insertion.insert_file_cos_matrix_brm_ifr()))
    except:
        print("Erreur lors de l'execution du script de similarité")
elif args.mturk:
    try:
        print(similarity.similarite(model, file_insertion.insert_file_mturk771()))
    except:
        print("Erreur lors de l'execution du script de similarité")
elif args.mc:
    try:
        print(similarity.similarite(model, file_insertion.insert_file_mc()))
    except:
        print("Erreur lors de l'execution du script de similarité")
elif args.rel:
    try:
        print(similarity.similarite(model, file_insertion.insert_file_rel122()))
    except:
        print("Erreur lors de l'execution du script de similarité")
elif args.simlex:
    try:
        print(similarity.similarite(model, file_insertion.insert_file_simlex999()))
    except:
        print("Erreur lors de l'execution du script de similarité")
elif args.analogie:
    try:
        analogie.analogie_GoogleQuestionWords(model)
    except:
        print("Erreur lors de l'execution du script d'analogie")
# elif args.umnsrs:
#    print(similarity.similarite(model, file_insertion.insert_file_UMNRS_similarity()))
elif args.wordsim:
    try:
        print(similarity.similarite(model, file_insertion.insert_file_wordsim()))
    except:
        print("Erreur lors de l'execution du script de similarité")

#ANALOGIE

