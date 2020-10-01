ficha = list()
while True:
    nome = str(input(f'Digite o nome: '))
    nota1 = float(input(f'Nota 1: '))
    nota2 = float(input(f'Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome,[nota1 , nota2], media])
    res = str(input('Quer continuar [S/N]'))
    if res in 'Nn':
        break
print(f'{"No":<4}{"Nome":<20}{"Média":<20}')
for i,a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<20} {a[2]:<20}')
while True:
    sair = int(input('Mostrar notas de qual aluno? para parar 999 '))
    if sair == 999:
        break
    if sair <= len(ficha)-1:
        print(f'As notas do aluno {ficha[sair][0]} são {ficha[sair][1]}')
