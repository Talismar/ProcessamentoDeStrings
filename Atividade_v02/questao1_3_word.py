from os import system
import keyboard 
import platform
system('cls')

if platform.system() == "Windows":
    system('cls')
else:
    system('clear')

"Importando os dados"
with open("C:\\Users\\talis\\Downloads\\corpus.txt", 'r', encoding="UTF-8") as data:
    words = data.read().lower()
    data.close()

print('Arquivo carregado')
def func_searc():
    word = (input('Informa a palavra -> ').lower())
    
    quant = (words.count(word))
    print('Quantidade >: ',quant)

keyboard.add_hotkey('ctrl', lambda : func_searc()) 
keyboard.wait('esc')