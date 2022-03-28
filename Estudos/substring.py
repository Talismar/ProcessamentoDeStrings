from os import system
system('cls')
word = 'Está'

"Substrings"
[print(word[:i+1]) for i in range(0,len(word))]

import string
def tem_caractere_ilegal(s):
    return any(c not in string.ascii_letters for c in s)

print(tem_caractere_ilegal(word))