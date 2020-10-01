Temp = []
Principal = []
mais = menos = 0
continua = ' '
while True:
    Temp.append(str(input(f'Digite o nome: ')))
    Temp.append(float(input('Digite o peso: ')))
    if len(Principal) == 0:
        mais = menos = Temp[1]
    else:
        if Temp[1] < menos:
            menos = Temp[1]
        if Temp[1] > mais:
            mais = Temp[1]
    Principal.append(Temp[:])
    Temp.clear()
    continua = ' '
    while continua not in 'SN':
        continua = str(input(f'Deseja continuar [S/N] ')).strip().upper()
    if continua == 'N':
        break
print(f'Você registrou {len(Principal)} pessoas')


for p in Principal:
    if p[1] >= mais:
        print(f'Os mais pesados foram {p[0]}', end=' ')
print(f'com maior peso foi {mais}', end='')
print()
for p in Principal:
    if p[1]<= menos:
        print(f'Os mais leves foram {p[0]}', end=' ')
print(f'com menor peso foi {menos}')