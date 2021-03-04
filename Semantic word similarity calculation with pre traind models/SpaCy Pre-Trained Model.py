# Importing Library
import spacy

# Loading pacy Trained model
# You will need the address of the directory that we have discussed in download step and that directory contain model details and files
# change the address in load method
# for the address was
# 'C:/Users/Khalil/Documents/PythonProjects/PyCharm/Top Word2Vec Models/en_core_web_lg-2.1.0/en_core_web_lg/en_core_web_lg-2.1.0')
nlp = spacy.load('C:/Users/Khalil/Documents/PythonProjects/PyCharm/Top Word2Vec Models/en_core_web_lg-2.1.0/en_core_web_lg/en_core_web_lg-2.1.0')
# Making Tokens
tokens = nlp('woman man')
# printing the similarity score between two tokens
print("Similarity Between ",tokens[0],'and',tokens[1],tokens[0].similarity(tokens[1]))
# Making Tokens
tokens = nlp("hotel motel")
# printing the similarity score between two tokens
print("Similarity Between ",tokens[0],'and',tokens[1],tokens[0].similarity(tokens[1]))
# Making Tokens
tokens = nlp("milk tea")
# printing the similarity score between two tokens
print("Similarity Between ",tokens[0],'and',tokens[1],tokens[0].similarity(tokens[1]))