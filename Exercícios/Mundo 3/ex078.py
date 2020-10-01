lista = []
mai = men = posMa = posMe = 0
for v in range (0,5):
      lista.append(int(input(f'Valor {len(lista)}: ')))
      if v == 0:
          mai = men = lista[v]
      else:
          if men > lista[v]:
              men = lista[v]
          if mai < lista[v]:
              mai = lista[v]

print(f'O maior valor da sua lista é: {mai} e sua posição é ' ,end= ' ')
for i , c in enumerate(lista):
    if c == mai:
      print(f'{i}..' , end= ' ')
print()
print(f'O menor valor da sua lista é: {men} e sua posição é ', end=' ')
for i , c in enumerate(lista):
    if c == men:
        print(f'{i}..', end=' ')
print()


