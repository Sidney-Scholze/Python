from random import randint
print('Par ou Ímpar')
print('*'*20)
vitorias = total = 0
while True:
    eu = int(input('Diga um valor: '))
    pc = randint(0,11)
    total = pc + eu
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar ? ')).strip().upper()[0]
    print('Você jogou {} e o computador jogou {}. Total = {}'.format(eu,pc,total))
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou')
            vitorias +=1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            vitorias += 1
            print('Voce venceu')
        else:
            print('Voce perdeu')
            break
print('Voce teve {} vitorias'.format(vitorias))
