import unicodedata

string_velha = "Olá você está????"
string_nova = ''.join(ch for ch in unicodedata.normalize('NFKD', string_velha) 
    if not unicodedata.combining(ch))
print(string_nova)

from unicodedata import normalize

def remove_accents(input_str):
    return normalize('NFKD', input_str).encode('ASCII','ignore').decode('ASCII')

if __name__ == "__main__":
    print(remove_accents('áàãâäåª'))