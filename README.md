# PPDM2
### Word Embedding

##### Langages : Python (Gensim, Numpy, Scipy, Flask) and HTML (Material Design for CSS)
##### Find full documentation at https://armiage.github.io/PPDM2/

------------------ PROJECT DESCRIPTION ------------------

The objective of this project is to implement an application using artificial intelligence techniques to solve problems of similarity or analogy, using the technique of word embedding or word embeddings.

To measure the quality of a set of word vectors, we use metrics that measure their ability to solve questions:

Similarity: Datasets - WordSim 353, SimLex-999, TOEFL dataset, MEN, SemSim, etc.

Analogy: Datasets - Google Questions

------------------ GUIDE ------------------

###### 1 - Install Dependencies
```pip install -r requirements.txt```

###### 1.2 - Install Developpement Dependencies
If you want to use our projet in an IDE, please use following command
```pip install -r requirements_dev.txt```

###### 2 - Download model
Download Text8 at http://mattmahoney.net/dc/textdata.html
And put it in your root project folder then .\src\MODEL

###### 3 - Use as command line
Open a console, go in your root project folder

And type ```python main.py --help``` and get all option to use this project

###### 4 - Use as a website
In your favorite IDE launch BackServ.py
And go at the following URL http://127.0.0.1:5000

------
