matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_par = coluna3 = linha2 = 0
num = 0
for l in range(0,3):
     for c in range(0,3):
         num = int(input(f'Digite os valores {l} {c}: '))
         matriz [l][c] = num


for l in range(0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz [l] [c] % 2 == 0:
            soma_par += matriz [l] [c]

    print()
for l in range(0,3):
    coluna3 += matriz [l] [2]

print(f'A soma dos numeros pares é {soma_par}')
print(f'A soma da coluna 3º é {coluna3} ')
for c in range(0,3):
    if c == 0:
        linha2 = matriz [1][c]
    elif matriz[1][c] >= linha2:
        linha2 = matriz[1][c]

print(f'O maior numero da segunda linha é {linha2}')
