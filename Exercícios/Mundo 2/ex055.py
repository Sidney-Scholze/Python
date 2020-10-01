peso_maior = 0
peso_menor = 0
for count in range(1,6):
    print('---{}ª Pessoa---'.format(count))
    peso = int(input('Peso: '))
    if count == 1:
        peso_menor = peso
        peso_maior = peso
    else:
       if peso > peso_maior:
        peso_maior = peso
       if peso < peso_menor:
        peso_menor = peso
print('O maior peso lido foi {} quilos'.format(peso_maior))
print('O menor peso lido foi {} quilos'.format(peso_menor))



