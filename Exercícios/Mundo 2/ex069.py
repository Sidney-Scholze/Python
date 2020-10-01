idade = pessoas_maiores18 = homens_cadastrados = mulheres_menos20 = 0
while True:
    print('-' * 30)
    print('Cadastro')
    print('-' * 30)
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo  not in 'MF':
        sexo = str(input('Sexo [F/M]')).strip().upper()[0]
        continua = ' '
        if idade < 20  and sexo in 'F':
            mulheres_menos20 +=1
        if idade >= 18:
            pessoas_maiores18 +=1
        if sexo == 'M':
            homens_cadastrados +=1
    while continua not in 'SN':
        continua = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if continua == 'N':
     break
print('Pessoas com mais de 18: {}'.format(pessoas_maiores18))
print('Homens cadastrados: {}' .format(homens_cadastrados))
print('Mulheres com menos de 20 anos: {}'.format(mulheres_menos20))







