## Reto https://codember.dev/ CHALLENGE_04

import requests
#from collections import Counter


# Descargamos archivo

url = 'https://codember.dev/data/files_quarantine.txt'
with requests.get(url) as file:
    message01 = file.content.decode('utf-8')
message01 = message01.split('\n')
#print(message01)

def splitChecksum(file):
    indexSeparator = file.find('-')
    fileName = file[0:indexSeparator]
    checksum = file[indexSeparator+1:]
    return(fileName,checksum)

def genChecksum(filename):
    checksum = ""
    #print(filename)
    for caracter in filename:
        #print(caracter, filename.count(caracter))
        if (filename.count(caracter) == 1):
            checksum = checksum + caracter
    return (checksum)
        
contador = 0
for item in message01:
    file = splitChecksum(item)
    realChecksum = genChecksum(file[0])
    if (file[1] == realChecksum):
        contador = contador + 1
    if (contador == 33):
        print(realChecksum)
    
