import random
n = int(input('Adivinhe um numero entre 0 e 5: '))
n_ran = random.randrange(0,5)
if n == n_ran:
    print('Você acertou!')
else:
    print('Você errou')
print('o Numero sorteado foi {}!' .format(n_ran))