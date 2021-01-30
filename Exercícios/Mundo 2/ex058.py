import random
pc = random.randint(1,6)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Adivinhe um número entre 1 e 6: '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador > pc:
            dica = print('Dica é menor que {} !'.format(jogador))
        elif jogador < pc:
            dica = print('Dica é maior que {} '.format(jogador))

print('Voçê acertou em {} tentativas'.format(palpites))