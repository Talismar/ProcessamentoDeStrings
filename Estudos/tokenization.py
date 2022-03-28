from nltk.tokenize import word_tokenize
from os import system
system('clear')


X = "talismar"
Y = "thalismar"

# tokenization
X_list = word_tokenize(X.lower()) 
Y_list = word_tokenize(Y.lower())

print(Y_list)
print(X_list)