lista = [[], []]
valor = 0
for c in range (0,5):
    valor = int(input(f'Digite o {c}º numero'))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(lista)
