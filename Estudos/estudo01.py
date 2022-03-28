from os import system
import re
from unicodedata import normalize

system('cls')

"Importando os dados"
with open("C:\\Users\\talis\\Downloads\\corpus.txt", 'r', encoding="utf-8") as data:
     words = data.read()
     
""" 
print(
    words.count('a') + 
    words.count('á') + 
    words.count('à') + 
    words.count('ã') + 
    words.count('â') + 
    words.count('ä') + 
    words.count('å') + 
    words.count('ª')) 
"""

"Limpeza dos dados aqui"
""" 
t = re.sub(r'[_\|\n]'," ", words)
Dadoslimpo = re.sub(r'[^ |\w]+', "", t)

acentos = re.findall(r'[^a-zA-Z0-9]', Dadoslimpo)
listaAcentos = list(set(acentos)) 
"""

""" 
print(listaAcentos)
acentos = re.findall(r'[á-úà-ùâ-ûª]', Dadoslimpo) 
"""

"""
print("Aguarde")
listaAcentos = list(set(acentos))
print(listaAcentos) 
"""

""" 
def remove_accents(input_str):
    return normalize('NFKD', input_str).encode('ASCII','ignore').decode('ASCII')

inp = input("Search >: ").lower()
iterator = re.finditer(r"{}".format(inp) , words)

aux = 0
for match in iterator:
    aux += 1
    print(match.span())

print(aux) 
"""

""" print(re.search(r'Kit composto por 2 Vodkas Sueca Absolut Vanilia 1000ml cada',words))
print("Talismar\fFernandes Costa")
print(re.findall(r"[^\w]+",words[1845:2090])) """

"Lista os accentos" 
""" words_with_accents = findall(r'[^a-z0-9 ]',  words_without_accents)
list_accents = list(set(words_with_accents)) 
print(list_accents)  """