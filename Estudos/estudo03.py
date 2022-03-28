from os import system
from re import finditer
import keyboard 
import platform

if platform.system() == "Windows":
    system('cls')
else:
    system('clear')

"Importando os dados - 5"
with open("C:\\Users\\talis\\Downloads\\corpus.txt", 'r', encoding="utf-8") as data:
    words = data.read().lower()
    data.close()
    print("Dados prontos")

def func_searc():
        quant = 0

        word = input("Buscar > ").lower()
        iterator = finditer(r"{}".format(word) , words)

        for k in iterator:
            quant += 1
            #print((k.span()))

        print('Quantidade >: ', quant)

keyboard.add_hotkey('ctrl', lambda : func_searc()) 
keyboard.wait('esc')