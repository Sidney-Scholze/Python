lista = list()
while True:
    num = int(input(f'Digite varios valores: '))
    lista.append(num)
    continuar = ' '
    while continuar not in 'NS':
        continuar = str(input('Continuar ? [S/N]')).strip().upper()
    if continuar == 'N':
        break
if 5 in lista:
    print(f'O numero cinco existe e está na {lista.index(5) + 1} posição')
else:
    print(f'O numero cinco não existe na sua lista')
print(f'Foram digitados {len(lista)} numeros em sua lista')
lista.sort(reverse=True)
print(f'Lista ordenada em forma decrescente é {lista}')
