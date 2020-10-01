

def ficha(nome='<desconhecido>',gols=0):

    print(f'O jogador {nome} fez {gols} gols no campeonato')


nome = str(input('Nome do jogador: '))
gols = str(input(f'Quantos gols {nome} fez: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome,gols)

