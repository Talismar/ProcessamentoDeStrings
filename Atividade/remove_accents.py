from unicodedata import normalize

def remove_accents(input_str):
    return normalize('NFKD', input_str).encode('ASCII','ignore').decode('ASCII')

if __name__ == "__main__":
    print(remove_accents('áàãâäåª'))
    #print((remove_accents('T')))