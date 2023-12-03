## Reto https://codember.dev/ CHALLENGE_05

import requests
import re
#from collections import Counter


# Descargamos archivo

url = 'https://codember.dev/data/database_attacked.txt'
with requests.get(url) as file:
    message01 = file.content.decode('utf-8')
message01 = message01.split('\n')

cadena = "iuiu"

def isNumCar(cadena):
    isNotCadena = re.search('\W', row[0])
    #print(cadena, isNotCadena, cadena.find('_'))
    if (isNotCadena != None or cadena.find('_') != -1):
        print("NO es cadena")
        return False
    else:
        print("SI es cadena")
        return True

def isNumber(cadena):
    if (re.search('\D',cadena)):
        return False
    return True

def exist(cadena):
    print('cadena: ', cadena)
    if (cadena == ""):
        print("NO existe")
        return False
    else:
        print("SI existe")
        return True
def isEmail(cadena):
    arroba = cadena.find('@')
    punto = cadena.find('.')
    if (arroba > 1 and punto > arroba and punto < len(cadena)):
        return True
    return False

hiddenMessage = ""
for item in message01:
    row = item.split(',')
    print (row)
    if (not exist(row[1])):
        continue
    elif (not exist(row[0])):
        hiddenMessage = hiddenMessage + row[1][0]
    elif (not isNumCar(row[0]) or not isNumCar(row[1])):
        hiddenMessage = hiddenMessage + row[1][0]
    elif not isEmail(row[2]):
        hiddenMessage = hiddenMessage + row[1][0]
        continue
    elif exist(row[3]) and not isNumber(row[3]):
        hiddenMessage = hiddenMessage + row[1][0]
    
    
    print(hiddenMessage)
    
    #print(row)
    #print(row[2], isEmail(row[2]))
    
