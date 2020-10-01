idade = int(input('Qual a idade do atleta ?: '))

if idade <= 9:
    print('Atleta mirim')
elif idade <= 14:
    print('Atleta Infantil')
elif idade <= 19:
    print('Atleta Junior')
elif idade <= 25 :
    print('Atleta Sênior')
else:
    print('Atleta Master')
