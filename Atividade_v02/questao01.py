from os import system
from remove_accents import remove_accents
from re import sub
from keyboard import add_hotkey, wait
system('cls')

"Importando os dados"
def import_dados():
    with open("C:\\Users\\talis\\Downloads\\corpus.txt", 'r', encoding="utf-8") as data:
        words = data.read().lower()
    data.close()

    "Limpeza dos dados aqui - 1"
    clean_data = sub(r'[_\|\n ]+'," ", words)
    clean_data = sub(r'[^\w]+', " ", clean_data)
    """ words = words.replace('_'," ")
    clean_data = sub(r'[^\n\w]+'," ", words) """

    words_without_accents = remove_accents(clean_data)
    print('Dados limpo')

    with open("C:\\Users\\talis\\Desktop\\Clean_data.txt", 'w') as arq:
        arq.write(words_without_accents)
        arq.close()

"Dados limpo"
with open("C:\\Users\\talis\\Desktop\\Clean_data.txt", "r",encoding="utf-8") as data:
    clean_data = data.read()

"Token - 2"
data_token = clean_data.split()
print('Dados OK')

"Buscador - 3"
def func_searc():
    word = input('Digite ').lower()
    word = remove_accents(word)
    print(data_token.count(word))

add_hotkey('ctrl', lambda : func_searc()) 
wait('esc')