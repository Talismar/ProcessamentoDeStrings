from os import system
import keyboard 
system('cls')

"Importando os dados"
with open("C:\\Users\\talis\\Downloads\\corpus.txt", 'r', encoding="utf-8") as data:
    words = data.read().lower()
    data.close()

word = []
quant = []
aux = 0

def func_searc():
    global word
    global quant
    global aux

    word.append(input('Digite ').lower())
    quant.append(words.count(word[aux]))
    print(quant[aux])
    aux += 1

keyboard.add_hotkey('ctrl', lambda : func_searc()) 
keyboard.wait('esc')