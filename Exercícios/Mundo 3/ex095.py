time = []
Dic = {}
Lis =[]

while True:
    Dic.clear()
    Dic['nome'] = str(input('Nome do jogador: '))
    partidas = (int(input(f'Quantas partidas {Dic["nome"]} jogou ')))
    Lis.clear()
    for p in range (0,partidas):
        Lis.append(int(input(f'Quantas gols {Dic["nome"]} fez na {p+1} partida ')))
    Dic['gols'] = Lis[:]
    Dic['total'] = sum(Lis)
    time.append(Dic.copy())

    while True:
        res = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if res in 'SN':
            break
        print('Digite S ou N')
    if res == 'N':
        break
print('-'*40)
print('Cod ',end='')
for i in Dic.keys():
    print(f'{i:<15}',end='')
print()
for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador ? [999] para parar'))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro não existe')
    else:
        print(f'Levantamento de jogador {time[busca]["nome"]}')
        for i ,g in enumerate(time[busca]["gols"]):
            print(f'No jogo {i+1} fez {g} gols')
