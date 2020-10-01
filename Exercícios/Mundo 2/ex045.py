import random
from time import sleep

print('\033[1;30;46mJO\033[m',end='')
sleep(1)
print('\033[1;30;46mKEN\033[m',end='')
sleep(1)
print('\033[1;30;46mPÔ\033[m')

print('''Opções
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador = int(input('Qual sua scolha ?:'))
computador_escolhas = ['pedra','papel','tesoura']
computador = random.choice(computador_escolhas)
humano_escolhas = ('pedra','tesoura','papel')
humano =(humano_escolhas[1-jogador])

print('Voce escolheu {}'.format(humano_escolhas[1-jogador]))
#jogada = str(humano_escolhas[jogador])
sleep(0.25)
print('.',end='')
sleep(0.1)
print('..',end='')
sleep(1.5)
print('...')

if humano == 'pedra' and computador == 'tesoura':
    print('Jogador escolheu   {}\nComputador escolheu  {}'.format(humano,computador).upper())
    print('Voce ganhou !!!')
elif humano == 'papel' and computador == 'pedra':
    print('Jogador escolheu   {}\nComputador escolheu  {}'.format(humano, computador).upper())
    print('Voce ganhou !!!')
elif humano == 'tesoura' and computador == 'papel':
    print('Jogador escolheu   {}\nComputador escolheu  {}'.format(humano, computador).upper())
    print('Voce ganhou !!!')
elif humano == computador:
    print('Empate\nComputador também escolheu   {}'.format(computador).upper())

else:
    print('Jogador escolheu   {}\nComputador escolheu  {}'.format(humano, computador).upper())
    print('Voce perdeu!!!')
