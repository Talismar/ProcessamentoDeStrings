from sklearn.metrics.pairwise import cosine_similarity
from os import system
from remove_accents import remove_accents
import re
system('cls')
with open("C:\\Users\\talis\\Desktop\\Clean_data.txt", 'r', encoding="utf-8") as data:
    words = data.read().lower()
    data.close()

string01 = 'pneu pirelli'
space_num = re.sub(r' +', ' ', string01).count(' ')
#print(re.findall(r' +[a-z]',string01))
X_list = list(string01)
print(X_list)
words = words.split()
for i in range(0,len(words)-space_num+1):
    
    #string02 = remove_accents(' '.join(map(str, words[i:i+space_num+1])))
    string02 = ' '.join(map(str, words[i:i+space_num+1]))
    
    
    Y_list = list(string02)

    X_set = []
    for i,j in zip(X_list, Y_list):
        if i != j:
            X_set.append(i)

    rvector = set(X_set+Y_list) 
    #print(rvector)
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

    #print(l1)
    #print(l2)
    if cosine_similarity([l1],[l2])[0][0] >= 0.95:
        print(Y_list)
        print(cosine_similarity([l1],[l2])[0][0])
        print(string02)