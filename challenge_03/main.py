## Reto https://codember.dev/ CHALLENGE_02

import requests
from collections import Counter


# Descargamos archivo y convertimos su contenido binario en un string

url = 'https://codember.dev/data/encryption_policies.txt'
with requests.get(url) as file:
    message01 = file.content.decode('utf-8')
message01 = message01.split('\n')

def checkKey(cadena):
    guionIndex = cadena.find('-')
    espacioIndex = cadena.find(' ')
    dosPuntosIndex = cadena.find(':')
    
    minimo = cadena[0:guionIndex]
    maximo = cadena[guionIndex+1:espacioIndex]
    letraClave = cadena[espacioIndex+1:dosPuntosIndex]
    clave = cadena[dosPuntosIndex+2:]
    #print(cadena, minimo, maximo, letraClave, clave)
    #number = cadena.count(letraClave)
    number = Counter(clave)[letraClave]
    if number < int(minimo) or number > int(maximo):
        return (False, clave)
    else:
        return (True, clave)

contador = 0
for item in message01:
    res = checkKey(item)
    if not res[0]:
        contador = contador + 1
    if contador == 42:
        print(res[1])