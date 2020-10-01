sexo = str(input('Digite seu sexo [M/F] ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input(str('Invalido: ')).strip().upper()[0]
print('Sexo digitado com sucesso {}'.format(sexo))


