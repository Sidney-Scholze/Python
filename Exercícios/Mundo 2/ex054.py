from datetime import date
count=0
numeroPerguntas = 4

for c in range (1,numeroPerguntas+1):
    ano_nascimento = int(input('Ano de nascimento {}º pessoa: '.format(c)))    
    if 21 > (date.today().year - ano_nascimento):
        count += 1
print('{} pessoas são maiores de 21 anos'.format(numeroPerguntas - count))
print('{} pessoas são menores de 21 anos'.format(count))
