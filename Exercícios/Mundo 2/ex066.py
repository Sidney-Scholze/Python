num = total = soma = 0
while True:
    num = int(input('Digite um valor [999] para parar: '))
    if num == 999:
        break
    else:
        total += 1
        soma += num
print('O total de numeros digitados foi: {} e soma entre eles foi: {}'.format(total,soma))