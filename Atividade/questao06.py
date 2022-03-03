from questao1_3_word import word, quant


with open('saveInformation.txt', 'w') as saveInf:

    saveInf.write("Informações da questão 03\n")
    for i,j in zip(word,quant):
        saveInf.write(f'A palavra {i} existe no texto {j}\n')

    saveInf.write("Informações da questão 04\n")
    for i, j in zip():
        pass

    saveInf.write("Informações da questão 05\n")
    for i, j in zip():
        pass
    
saveInf.close()