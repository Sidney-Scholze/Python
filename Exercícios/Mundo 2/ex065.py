num = count = menor = maior = média = 0
resp = 'S'

while resp in 'Ss':
    num = int(input('Digite um numero inteiro: '))
    resp = str(input('Deseja continua ? [S/N}')).upper().strip()[0]
    if menor == 0:
        menor = num

    if num < menor and num != 0:
        menor = num

    elif num > maior:
        maior = num
    count += 1
    média += num
média = média / count
print('Voce digitou {} números a média foi {}'.format(count,média))
print('O maior foi {} e o menor foi {}'.format(maior, menor))