import string
import os 
os.system('cls')

s = "Olá, mundo!"

# A string s começa com "Olá"?
#print(s.startswith("Olá"))

# A string s termina com "mundo"?
#print(s.endswith("mundo!"))

import re
#print(re.subn(r'O',r'ba',s))

"Inverter as letras"
print(s.swapcase())

'Corta string com espaço'
#print(s.split())

""
s = 'talismar'
#print(s.find('a'))
from pprint import pprint
lista = "Talismar','Fernandes', 'Costa'"
pprint(re.findall(r'\w+', lista))