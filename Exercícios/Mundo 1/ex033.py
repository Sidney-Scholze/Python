n1 = int(input('digite 1º numero: '))
n2 = int(input('digite 2º numero: '))
n3 = int(input('digite 3º numero: '))
menor = n1
maior = n2

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor digitado foi {}' .format(menor))

if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n2 and n3 > n1:
    maior = n3
print('O maior numero digitado foi {}'.format((maior)))


