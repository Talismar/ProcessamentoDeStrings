from os import system
import re
import string
system('cls')

with open('D:\Algoritmos\DisciplinaAlgoritmo\ProcessamentoString\palavra.txt', 'r', encoding="utf-8") as data:
     words = data.read()

"Limpeza dos dados aqui"
print(re.findall(r'[/\W|_/]', words))
t = re.sub(r'[_\n]'," ", words)
print(re.findall(r'[^ |\w\n]+', words))
print(re.sub(r'[^ |\w\n]+', "", t))

"Ignorando as letras maiusculas"
#print(re.findall(r'[a-z]+', words, flags=re.IGNORECASE))
#print(re.findall(r'\w+', words, flags=re.IGNORECASE))

"Pesquisando palavras que começa com ->"
""" while True:
     entr = input('Digite ')
     print(re.findall(r'\b{}\w+'.format(entr), words, flags=re.I)) """
"Pesquisando palavras que termina com ->"
#print(re.findall(r'\w+e\b', words, flags=re.I))

print(words)



#print(re.search(r'Que'.lower(), words.lower()))
#print(re.findall(r'Que'.lower(), words.lower()))
token = ' '
#words = re.sub(token,' ', words)
#print(words)
"Aqui se refere ao token que eu estou usando para separar que é o ' '"
dados = words.split()
#print(dados)
""" d = re.split(f'{token}',words)
print(d) """

"Qualquer caracter com exceção a quebra de linha"
#print(re.findall(r'res....do', words))
"Conjunto de caracter"
#print(re.findall(r'[Qq]ue', words))

#print(re.findall(r'qUe', words, flags=re.IGNORECASE))