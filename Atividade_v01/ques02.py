"Token dos dados - espaços"
def token(words):
    return words.split()

"Importando um novo arquivo limpo"
def new_file(words_without_accents):
    with open("C:\\Users\\talis\\Desktop\\New_Clean_data.txt", 'w') as arq:
        arq.write(words_without_accents)
        arq.close()
    return "C:\\Users\\talis\\Desktop\\New_Clean_data.txt"