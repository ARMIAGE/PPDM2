import unittest
import file_insertion
import similarity
import fonctions_utiles
import numpy as np

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_matriceRGNotNull(self):
       data = file_insertion.insert_file_rg()
       self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()