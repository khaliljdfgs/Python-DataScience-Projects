from gensim.models.keyedvectors import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec

# replace the address of glove_input_file in below code line. Use the address of the downloaded "glove.6B.300d.txt" file address
# replace the word2vec_output_file address in below code line this will be a new file that we genrate from "glove.6B.300d.txt"
glove2word2vec(glove_input_file="C:/Users/Khalil/Downloads/Compressed/glove.6B/glove.6B.300d.txt", word2vec_output_file="C:/Users/Khalil/Downloads/Compressed/glove.6B/gensim_glove_vectors6b.txt")

# In below line use the same path that you have used as word2vec_output_file in above code line
model = KeyedVectors.load_word2vec_format("C:/Users/Khalil/Downloads/Compressed/glove.6B/gensim_glove_vectors6b.txt", binary=False)


# Printing the similarity score between two words
print("Similarity Between Woman and Man" , model.similarity('woman',"man"))
print("Similarity Between Hotel and Motel" , model.similarity('hotel',"motel"))
print("Similarity Between Milk and Tea" , model.similarity('milk',"tea"))