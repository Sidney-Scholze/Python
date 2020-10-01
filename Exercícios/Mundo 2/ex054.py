from datetime import date
count=0
ano_nascimento = 0

for c in range (1, 8,1):
    ano_nascimento = int(input('Ano de nascimento {}º pessoa: '.format(c)))
    #print('Idade = {}'.format(date.today().year - ano_nascimento))
    if 21 > (date.today().year - ano_nascimento):
        count += 1
print('{} pessoas são maiores de 21 anos'.format(c - count))
print('{} pessoas são menores de 21 anos'.format(count))
