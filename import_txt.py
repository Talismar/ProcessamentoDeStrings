from os import system

"Importando os dados"
with open("D:\\Algoritmos\\DisciplinaAlgoritmo\\ProcessamentoString\\palavra.txt", 'r', encoding="utf-8") as data:
     words = data.read().lower()