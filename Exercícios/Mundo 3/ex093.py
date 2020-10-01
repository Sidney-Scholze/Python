Dic = {}
Lis =[]
Dic['nome'] = str(input('Nome do jogador: '))
partidas = (int(input(f'Quantas partidas {Dic["nome"]} jogou ')))

for p in range (0,partidas):
    Lis.append(int(input(f'Quantas gols {Dic["nome"]} fez na {p+1} partida ')))
Dic['gols'] = Lis[:]
Dic['total'] = sum(Lis)
for k, v in Dic.items():
    print(f'O campo {k} tem valor {v}')
print(f'O jogador {Dic["nome"]} jogou {len(Lis)} vezes')
for i, v in enumerate(Dic['gols']):
    print(f'Na {i+1} partida, fez {v} gols')
print(f'Total de {Dic["total"]} gols')
print(Dic)
print(Lis)


