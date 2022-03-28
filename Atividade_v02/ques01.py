from re import sub
from unicodedata import normalize

"Pré-Processamento do Dataset"
def dataset(path):
    with open(path, 'r', encoding="utf-8") as data:
        words = data.read().lower()
        data.close()
    return words

def remove_accents(input_str):
    return normalize('NFKD', input_str).encode('ASCII','ignore').decode('ASCII')

"Limpeza dos dados"
def clean_dataset(words):
    #clean_data = sub(r'[_\| |\W]+'," ", words)
    words = words.replace('_'," ")
    clean_data = sub(r'[^\n\w]+'," ", words)

    "Remove accents"
    words_without_accents = remove_accents(clean_data)
    print('Dados limpo')
    return words_without_accents