dicionario ={}
lista = []

média = soma = 0

#soma += dicionario['idade']
while True:
    dicionario.clear()
    dicionario['nome'] = str(input('Nome: '))
    while True:
        dicionario['sexo']= str(input('Sexo [M/F]')).strip().upper()
        if dicionario['sexo'] in 'MF':
            break
        print('Erro por favor digite M ou F')
    dicionario['idade'] = int(input('Idade: '))
    soma += dicionario['idade']
    lista.append(dicionario.copy())
    while True:
        sair = str(input('Deseja continuar [S/N]')).upper()[0]
        if sair in 'SN':
          break
        print('Erro digite S ou N')
    if sair == 'N':
        break



print(f'{len(lista)} pessoas foram cadastradas')
média = soma /len(lista)
print(f'A média de idade do grupo é {média:.1f} anos de idade')
print('As mulheres cadastradas foram: ',end=' ')
for p in lista:
    if p["sexo"] in 'Ff':
        print(f'{p["nome"]}',end=' ')
print()
print(f'Homens cadastrados: ',end='')
for p in lista:
    if p['sexo'] in 'Mm':
        print(f'{p["nome"]} ', end='')
print()
print('Pessoas acima da média: ')
for p in lista:
    if p['idade'] >= média:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print()


