alunos = dict()

alunos['nome'] = str(input(f'Nome: '))
alunos['média'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['média'] < 7:
    alunos['Situação'] = 'Reprovado'
else:
    alunos['Situação'] = 'Aprovado'
for k, v in alunos.items():
    print(f'{k} é igual a {v}')
