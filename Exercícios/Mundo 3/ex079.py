lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor Duplicado')
    else:
        print('Valor inserido com sucesso')
        lista.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp == 'N':
     break
lista.sort()
print(lista)
