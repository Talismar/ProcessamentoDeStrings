from re import sub, findall
from unicodedata import normalize

def remove_accents(input_str):
    return normalize('NFKD', input_str).encode('ASCII','ignore').decode('ASCII')

word = 'talísmar/* +- \n\n  %$#@@#   £¢¬£³²¹°ºªª´´``^^~~;t .+/?^~]][`{~~´_/\`{   Anm,Ps....adLKmas'

"Remove tudo menos os \n do texto - Regex"
clean_data = word.replace('_'," ")
clean_data = sub(r'[^\n\w]+', " ", remove_accents(clean_data))

print(clean_data)