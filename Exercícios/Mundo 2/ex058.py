import random
pc = random.randint(0,5)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Adivinhe um numero entre 0 e 10: '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador > pc:
            dica = print('Dica é menor que {} !'.format(jogador))
        elif jogador < pc:
            dica = print('Dica é maior que {} '.format(jogador))

print('Voçê acertou em {} tentativas'.format(palpites))