import random
import os
import datetime
import json

'''class User(object):
    def __init__(self, nome, record):
        self.nome = nome
        self.record = record'''

start = datetime.datetime.now()
clear = lambda: os.system('cls')
sorteio = random.randint(0,100)
clear()

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

'''with open('database.json') as json_data:
    d = json.load(json_data)

recordes : User = Payload(d)
print(recordes)
'''
print("Bem vindo, escolha um numero de 0 a 100 :B")

tentativas = 1
while(True):
    numero = int(input("Numero : "))

    if numero < sorteio:
        print("ERRROOOU! É maior que isso")
    elif numero > sorteio:
        print("ERROOOOU! É menos que isso")
    else:
        print("Acertooou mizerávi")
        break
    tentativas += 1

end = datetime.datetime.now()

print("\n\n\nVocê completou em : " + str((end - start).total_seconds()))
print("Um total de " + str(tentativas) + " tentativas")
