s = 0
for n in range(1,7,1):
    num = int(input('Digite o {}º valor: '.format(n)))
    if num % 2 == 0:
        s += num
print('A soma dos numeros pares = {}'.format(s))

