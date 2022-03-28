import string

def has_accents(s):
    stringOri = ""
    numeros = []
    
    for i in s:
        if i not in string.ascii_letters:
            #print(i)
            numeros.append(i)
        stringOri = stringOri + i
    
    #return list(set(numeros))
    return any(c not in string.ascii_letters for c in s) 

print(has_accents('tálís'))