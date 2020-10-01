from datetime import date
ano = int(input('Digite um ano ou\nDigite "0" para ano atual: '))
if ano == 0:ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} {} {} é um ano bissexto'.format('\033[1;32m',ano,'\033[m'))
else:
    print('{}{}{} não é um ano bissexto' .format('\033[1;31m',ano,'\033[m'))

