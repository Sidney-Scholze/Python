saque_total = cedulas = count50 = count20 =  0
print('\n{:.^50} \n\nCédulas de R$ 1.00 | R$ 10.00 | R$ 20.00 | R$ 50.00'. format('Saque eletronico'))
saque_total = int(input('Qual o valor do saque? '))
total = saque_total
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print('Total de {} cedulas de R${}'.format(total_cedula,cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
             break
