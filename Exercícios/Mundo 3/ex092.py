from datetime import datetime
ficha ={}


ficha['Nome'] = str(input(f'Nome: '))
nas = int(input('Ano de nascimento: '))
ficha['Idade'] = datetime.now().year - nas
ficha['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if ficha['ctps']!= 0:
    ficha['Ano de contratação'] = int(input('Ano de contratação: '))
    ficha['Salário'] = float(input('Salário: '))
    ficha['Aposentadoria'] = ficha['Idade']+((ficha['Ano de contratação']+35) - datetime.now().year)
for k,i in ficha.items():
    print(f'{k} = {i}')

