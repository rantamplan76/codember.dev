## Reto https://codember.dev/ CHALLENGE_01

import requests


# Descargamos archivo y convertimos su contenido binario en un string

url = 'https://codember.dev/data/message_01.txt'
with requests.get(url) as file:
    message01 = file.content.decode('utf-8')
message01 = message01.strip('\n')
# creamos un diccionario con las palabras como indice y el numero de occurencias como valor

word_counter = {}

'''por cada palabra en el string comprobamos si existe en el array.
Si existe incrementamos uno el valor y sino creamos una nueva clave con valor uno
'''

for word in message01.split(' '):
    if word in word_counter.keys():
        word_counter[word] = word_counter[word] + 1
    else:
        word_counter[word] = 1
#print(word_counter)
#print(word_counter.keys())

# convertimos el array en una cadena de texto concatenando claves y valores
res = ''
for item in word_counter:
    res= res + item + str(word_counter[item])

print(res)
