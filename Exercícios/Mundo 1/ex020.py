from random import shuffle
print('Ordem de apresentação')
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
lista = [a,b,c]
shuffle(lista)
print(lista)
