import unittest
import file_insertion
from gensim.models import word2vec
import similarity
import fonctions_utiles
import numpy as np

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_matriceRGNotNull(self):
       data = file_insertion.insert_file_rg()
       self.assertIsNotNone(data)

    def test_motConnu(self):
       data = file_insertion.insert_file_simlex999()
       self.assertEqual(data[1,0], "smart")

    def test_longueurConnu(self):
        data = file_insertion.insert_file_rel122()
        self.assertEqual(np.size(data), 366)

    def test_MotConnu2(self):
        data = file_insertion.insert_file_simlex999()
        self.assertIn("new", data)

    def test_MotInconnu(self):
        data = file_insertion.insert_file_simlex999()
        self.assertNotIn("abc123", data)

    def test_matriceNotNul(self):
        data = fonctions_utiles.extract_liste_de_mots(file_insertion.insert_file_simlex999())
        self.assertIsNotNone(data)

    def test_Ratio(self):
        taux = fonctions_utiles.calcul_corellation(1,2)
        self.assertIsNotNone(taux)

    def test_GetModel(self):
        model = word2vec.Word2Vec.load('../MODEL/W2V_text8_Model.bin')
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()