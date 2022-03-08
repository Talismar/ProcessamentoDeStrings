from ques01 import dataset, clean_dataset
from ques02 import token, new_file
from os import system
import platform

if platform.system() == "Windows":
    system('cls')
else:
    system('clear')

words = dataset("C:\\Users\\talis\\Downloads\\corpus.txt")
words = clean_dataset(words)
words_token = token(words)
new_words = new_file(words)

def open_new_file():
    with open("C:\\Users\\talis\\Desktop\\New_Clean_data.txt", 'r', encoding="UTF-8") as new_words:
        words = new_words.read()
        new_words.close()
        return words

#print(open_new_file())
#print(words_token)