from os import system
from re import finditer

system('cls')

"Importando os dados - 5"
with open("C:\\Users\\talis\\Downloads\\corpus.txt", 'r', encoding="utf-8") as data:
     words = data.read().lower()

inp = input("Buscar > ").lower()
iterator = finditer(r"{}".format(inp) , words)

quant = 0
for match in iterator:
    quant += 1
    #print(match.span())

print("Total de palavras encontrada ",quant)