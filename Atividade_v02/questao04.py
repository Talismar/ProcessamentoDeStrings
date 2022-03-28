from sklearn.metrics.pairwise import cosine_similarity
from os import system
from remove_accents import remove_accents
import itertools
import re

system('cls')
with open("C:\\Users\\talis\\Desktop\\Clean_data.txt", 'r', encoding="utf-8") as data:
    words = data.read().lower()
    data.close()

string01 = 'pneu  pirelli'
string01, space_num = re.sub(r' +', ' ', string01), re.sub(r' +', ' ', string01).count(' ') + 1 

X_list = list(string01)
print(X_list)
print(space_num)

words = words.split()
for i in range(0,len(words)-space_num):
    
    #string02 = remove_accents(' '.join(map(str, words[i:i+space_num])))
    string02 = ' '.join(map(str, words[i:i+space_num]))
    
    Y_list = list(string02)

    X_set = []
    for i,j in itertools.zip_longest(X_list, Y_list, fillvalue=""):
        if i != j:
            X_set.append(i)
        if i == "":
            X_set.remove(i)

    rvector = set(X_set+Y_list) 
    
    l1 =[]
    l2 =[]

    for w in rvector:
        if w in X_list: 
            l1.append(1)
        else: 
            l1.append(0)
        if w in Y_list:
            l2.append(1)
        else: 
            l2.append(0)

    if cosine_similarity([l1],[l2])[0][0] >= 0.90:
        print(Y_list)
        print(cosine_similarity([l1],[l2])[0][0])
        print(string02)