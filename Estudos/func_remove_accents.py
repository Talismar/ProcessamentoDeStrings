from unicodedata import normalize, combining
import re

def remove_accents(input_str):
    return normalize('NFKD', input_str).encode('ASCII','ignore').decode('ASCII')

def remove_car(strinf):
    normalized = normalize('NFD', strinf)
    return "".join([l for l in normalized if not combining(l)])

def remove_car02(strinf):
    normalized = normalize('NFD', strinf)
    return re.sub(r'[\u0300-\u036f]', "", normalized)

if __name__ == "__main__":
    print(remove_car('áàãâäåª'))