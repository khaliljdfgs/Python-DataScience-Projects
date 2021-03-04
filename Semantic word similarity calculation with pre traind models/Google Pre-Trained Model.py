# Importing Library
from gensim.models import KeyedVectors

# Loading Goolgle Trained model
model = KeyedVectors.load_word2vec_format('C:/Users/Khalil/Documents/PythonProjects/uni/Word Embeddings/GoogleNews-vectors-negative300.bin', binary=True)

# Printing the similarity score between two words
print("Similarity Between Woman and Man" , model.similarity('woman',"man"))
print("Similarity Between Hotel and Motel" , model.similarity('hotel',"motel"))
print("Similarity Between Milk and Tea" , model.similarity('milk',"tea"))