tupla = tuple(int(input('Digite um numero: '))for c in range(4))
print(f'Sua tupla é {tupla}')
print(f'O numero nove apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O primeiro valor 3 está na {tupla.index(3)+1}')
else:
    print(f'O valor 3 não foi encontrado')

print(f'Os valores pares digitados foram: ', end=' ')
for c in tupla:
    if c % 2 == 0:
        print (c, end=' ')
    else:
        print(f'0')
        break

