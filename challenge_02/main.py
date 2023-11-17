## Reto https://codember.dev/ CHALLENGE_02

import requests


# Descargamos archivo y convertimos su contenido binario en un string

url = 'https://codember.dev/data/message_02.txt'
with requests.get(url) as file:
    message01 = file.content.decode('utf-8')
message01 = message01.strip('\n')

#res = ""

#for caracter in message01:
#    print(caracter)

class compiler:
    numero = 0
    cadena = ""
    
    def operacion(self, operador):
        if operador == "#":
            self.incremento()
        if operador == "@":
            self.decremento()
        if operador == "*":
            self.multiplica()
        if operador == "&":
            self.imprime()
    
    def incremento(self):
        self.numero = self.numero + 1
    
    def decremento(self):
        self.numero = self.numero - 1
        
    def multiplica(self):
        self.numero = self.numero * self.numero
    
    def imprime(self):
        self.cadena = self.cadena + str(self.numero)
        
    def getNumero(self):
        return self.numero
    
    def getCadena(self):
        return self.cadena
    

res = compiler()

for caracter in message01:
    res.operacion(caracter)
"""while True:
    comando = input("Escribe un comando (# @ * &):")
    if comando == "0":
        break
    res.operacion(comando)
"""
print(res.getCadena())
print(res.getNumero())