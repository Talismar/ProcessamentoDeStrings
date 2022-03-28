from os import system
import keyboard 
import string
import re
system('cls')

text = 'O que me faz pressupor que ainda não temos marketing nas bibliotecas brasileiras é o resultado de tudo isso acima, mas que se conclui principalmente em virtude'
""" mytable = text.maketrans({'é':'e'})
print(text.partition('O')) """
mytable = text.maketrans({' ':'-','m':'t'})
print(text.translate(mytable))

texto = 'arara'
padrao = re.compile('ar.ra')
check = padrao.findall(texto)
print(check)

""" 
texto = 'atlksjlkdfsl'
"Verifica se o primeiro caracter é a"
padrao = re.compile('^a')
"Torna os demais caracteres diferente de a"
padrao = re.compile('[^a]')
check = padrao.findall(texto)
print(check) 
"""

""" 
texto = 'arara1992'
"Verificando se existe numero na string"
p = re.compile(r'\d')
c = p.findall(texto)
print(c)

 """
""" 
texto = 'arara1992'
"Verificando se existe caracter na string"
p = re.compile(r'\D')
c = p.findall(texto)
print(c)
 """
""" 
texto = '''

arara1992
'''
"Pegando os caracter especiais como quebra de linha e espaco"
p = re.compile(r'\s')
c = p.findall(texto)
print(c)
 """
"""  
texto = '''

arara1992
'''
"Retorna tudo sem espacos e quebra de linha"
p = re.compile(r'\S')
c = p.findall(texto)
print(c)
 """
""" 
texto = '''

_arara@ 1992_
'''
"Retorna todos os caracteres que sao alfanumerico \w e \W retorna ao contrario"
p = re.compile(r'\W')
c = p.findall(texto)
print(c)
 """

""" 
texto = '''ararab'''

p = re.compile(r'b')
c = p.findall(texto)
cm = p.search(texto)
print(cm)
 """
""" 
texto = '''ararab'''

p = re.compile(r'a')
c = p.findall(texto)
cm = p.finditer(texto)
print(cm)

correspondencias = cm
for co in correspondencias:
    print(co)
 """

te = 'Arara 1992'

p = re.compile(r'[a-zA-Z0-9]')
c = p.finditer(te)

for i in c:
    pass

""" regex = re.compile(r'que')
print(regex.findall(words)) """


te = 'Arara 1992 ar 1988964'

#p = re.compile(r'[a-zA-Z] [0-9]')
p = re.compile(r'[a-zA-Z]+ [0-9]+')
c = p.finditer(te)

for i in c:
    pass
    #print(i)


te = 'Talismar'

#p = re.compile(r'[a-zA-Z] [0-9]')
p = re.compile(r'[A-Ztali]*')
c = p.finditer(te)

for i in c:
    pass
    #print(i)


te = 'Talismar Talismar'

#p = re.compile(r'[a-zA-Z] [0-9]')
p = re.compile(r'[A-Z][talis]+')
c = p.finditer(te)

for i in c:
    pass
    #print(i)


te = 'Talismar Talismar'

#p = re.compile(r'[a-zA-Z] [0-9]')
""" p = re.compile(r'[A-Z][talis]+')
c = p.finditer(te)
print()
for i in c:
    pass
    print(i)
 """





""" for i in range(text.count(esp)):
    print() """
""" print(text.find('me'))
print(text.rfind('me'))
print(text[-15])
print(text.replace(' ','-')) """

""" def searc():
    sea = input('Digite ')
    print(text.count(sea))

keyboard.add_hotkey('ctrl', lambda : searc()) 
keyboard.wait('esc')  """