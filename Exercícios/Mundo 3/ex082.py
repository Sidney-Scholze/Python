lista = list()
lista_par = list()
lista_impar = list()
while True:
    lista.append(int(input(f'Digite numeros: ')))
    maior = max(lista)
    lista.sort()
    for p in range(1,maior+1):
       if p in lista:
          if p % 2 == 0 and p not in lista_par:
              lista_par.append(p)
              lista_par.sort()

          elif p % 2 != 0 and p not in lista_impar:
              lista_impar.append(p)
              lista_impar.sort()
    c = ' '
    while c not in 'SN':
         c = str(input(f'Continua? [S/N] ')).strip().upper()
    if c == 'N':
     break
print(f'A lista completa é: {lista}')
print(f'Numeros pares são: {lista_par}')
print(f'Os numeros impares: {lista_impar}')
