import docx2txt

#!read in word file
result = docx2txt.process("C:\\Users\\talis\\Desktop\\Dados_Algoritmo.docx")

if __name__ == "__main__":
    print(result)