import random
a = input('Aluno 1: ')
b = input('Aluno 2: ')
c = input('Aluno 3: ')
d = input('Aluno 4: ')
lista = [a,b,c,d]
aluno = random.choice(lista)
print('O aluno que vai apagar o quadro é {}' .format(aluno))
