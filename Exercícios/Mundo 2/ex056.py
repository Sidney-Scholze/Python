média_idade = 0
idade_mais_velho = 0
nome_mais_velho = 'Não existe'
mulheres_menos_20 = 0
for c in range(1,5):
    print('----{}º pessoa----'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade:'))
    sexo = input('Sexo F / M: ').strip().lower()
    média_idade += idade
    if idade > idade_mais_velho and sexo == 'm':
        idade_mais_velho = idade
        nome_mais_velho = nome

    if sexo == 'f' and idade < 20:
        mulheres_menos_20 += 1

print('Á média de idade das {} pessoas é {:.1f} anos'.format(c,média_idade / c))
print('Nome do homem mais velho é {} e tem {} anos'.format(nome_mais_velho,idade_mais_velho))
print('Ao todo são {} mulheres com  menos de 20 anos'.format(mulheres_menos_20) )
