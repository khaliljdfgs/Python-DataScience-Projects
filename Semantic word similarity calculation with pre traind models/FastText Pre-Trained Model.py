# Importing library
import gensim

# loading pre-trained model
# Past your model address in load_word2vec_format method in below line
model = gensim.models.KeyedVectors.load_word2vec_format('C:/Users/Khalil/Documents/PythonProjects/PyCharm/Top Word2Vec Models/wiki-news-300d-1M-subword.vec')

# Printing the similarity score between two words
print("Similarity Between Woman and Man" , model.similarity('woman',"man"))
print("Similarity Between Hotel and Motel" , model.similarity('hotel',"motel"))
print("Similarity Between Milk and Tea" , model.similarity('milk',"tea"))