from sklearn.metrics.pairwise import cosine_similarity
from remove_accents import remove_accents
from time import sleep
import itertools
from os import system
import keyboard 
import platform
from re import finditer, sub

if platform.system() == "Windows":
    system('cls')
else:
    system('clear')

aux = True
"Importando os dados"
with open("C:\\Users\\talis\\Downloads\\corpus.txt", 'r', encoding="utf-8") as data:
    words = data.readlines()
    data.close()        
    print('Arquivo carregado')

def Questao03():
    global words
    def writeFile01(word, quant, pages, words):
        with open('saveInformation.txt', 'a') as saveInf:

            saveInf.write("\nInformações da questão 03\n")
            saveInf.write(f'A palavra {word} aparece no texto {quant} vezes')
            
            for j in pages:
                saveInf.write(f'\nLinha >: {j} # indices --> ')
                
                for i in range(len(words[j])):
                    if word == words[j][i:i+len(word)].lower():
                        saveInf.write(f'({i} : {i + len(word)}) - ')

        saveInf.close()
    
    def func_searc():
        word = (input('Digite ').lower())
        quant = 0

        pages = []
        for i, j in enumerate(words):
            if word in j.lower():
                quant += j.lower().count(word)
                pages.append(i)
                
        writeFile01(word, quant, pages, words)        
        pages.clear()

        print('Quantidade >: ',quant )
        

    keyboard.add_hotkey('ctrl', lambda : func_searc()) 
    keyboard.wait('esc')

#Questao03()

def Questao04():
    with open("C:\\Users\\talis\\Desktop\\Clean_data.txt", 'r', encoding="utf-8") as data:
        words04 = data.read().lower()
        data.close()
        print('Arquivo carregado')

    def open_file(file, word):
        file.write("\nInformações da questão 04\n")
        file.write(f"Informações da palavra {word} - Usando a similaridade Cosseno\n")

    def writeFile03(word, quant, porcentagem, indices):
        global aux
        with open('saveInformation.txt', 'a') as saveInf:
            if aux:
                open_file(saveInf, word)
                aux = False
                return

            if type(quant) == int:
                saveInf.write(f'\nExiste {quant} palavras no texto similar a {word}\n\n')
                saveInf.close()
                return

            saveInf.write(f'\nPorcentagem {round(porcentagem,4)} -- palavra --> {word}')
            saveInf.write(f" -- indices -> ({indices[0]} : {indices[1]})")

        saveInf.close()

    "Similaridade de texto - Cosseno"
    quant = 0
    string01 = 'desenvolvimento'
    string01, space_num = sub(r' +', ' ', string01), sub(r' +', ' ', string01).count(' ') + 1 

    writeFile03(string01, None, None, None)

    "Transformando string01 em list"
    X_list = list(string01)
    
    print("Quantidade de palavras que selecionara do texto para fazer a buscar --> ",space_num)

    "Token - Espaço"
    words04 = words04.split()
    for t in range(0,len(words04)-space_num):
        "Precorrendo todo o texto de acordo com a quantidade de palavras que o usuario digitou"
        string02 = ' '.join(map(str, words04[t:t+space_num]))
        
        "Transformando em list"
        Y_list = list(string02)

        X_set = []
        for i,j in itertools.zip_longest(X_list, Y_list, fillvalue=""):
            if i != j:
                X_set.append(i)
            if i == "":
                X_set.remove(i)
        
        rvector = list(set(X_set+Y_list)) 
        
        l1 =[]
        l2 =[]

        for w in rvector:
            if w in X_list: 
                l1.append(1)
            else: 
                l1.append(0)
            if w in Y_list:
                l2.append(1)
            else: 
                l2.append(0)

        
        if cosine_similarity([l1],[l2])[0][0] >= 0.80:
            quant += 1
            print(quant, ' - ', string02)
            writeFile03(string02, None, cosine_similarity([l1],[l2])[0][0], [t,t+space_num])
    
    writeFile03(string01, quant, None, None)

#Questao04()

def Questao05():
    global words
        
    def open_file(file, word):
        file.write("\nInformações da questão 05\n")
        file.write(f"Informações da palavra {word}\n")

    def writeFile02(word, indice ,quant, pages):
        global aux
        with open('saveInformation.txt', 'a') as saveInf:
            if aux:
                open_file(saveInf, word)
                aux = False

            if type(quant) == int:
                saveInf.write(f'\n{word} existe {quant} no texto\n\n')
                saveInf.close()
                return

            saveInf.write(f'\nLinha >: {pages} # indices --> ')
            saveInf.write(f'({indice[0]} : {indice[1]}) -- ')
            saveInf.write(f'quantidade em linha --> {quant.count(word)}')
            
        saveInf.close()
    
    def func_searc():
        global aux
        aux = True
        quant = 0

        word = input("Buscar > ").lower()
        
        for i, j in enumerate(words):
            if word in j.lower():
                iterator = finditer(r"{}".format(word) , j.lower())

                for k in iterator:
                    quant += 1
                    writeFile02(word, k.span(), j.lower(), i)
        
        print('Quantidade >: ', quant)
        writeFile02(word, None, quant, None)

    keyboard.add_hotkey('ctrl', lambda : func_searc()) 
    keyboard.wait('esc')

#Questao05()