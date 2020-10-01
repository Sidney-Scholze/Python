from random import randint
from time import sleep


def sorteia(lista):
    for cont in range(0,5):
        números.append(randint(1,10))

def somaPar(lista):
    soma = 0
    for p in lista:
        if p % 2 == 0:
            soma += p
    print(f' A soma dos numeros pares da lista {números} é {soma}')


números = list()
sorteia(números)
somaPar(números)
print(f'Numeros {números}')







