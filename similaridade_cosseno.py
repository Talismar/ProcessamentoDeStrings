import itertools
t1 = "alismar Fernandes Costa"
t2 = 'Talismar Fernandes Araujo'

print(t1)
X_set = []
for (i,j) in itertools.zip_longest(t1, t2, fillvalue=""):
    if i != j:
        X_set.append(i)
    if i == "":
        X_set.remove(i)


t2 = list(t2)
print(X_set)

rvector = set(X_set+t2)
print(rvector)

""" l1 =[]
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
 """