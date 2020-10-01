num = soma = total = 0
while num != 999:
    num = int(input('Digite um numero inteiro [999] para encerrar: '))
    #print('Digite 999 para encerrar')
    if num != 999:
        soma += num
        total += 1
print('A soma dos {} numeros digitados foi {}'.format(total,soma))
