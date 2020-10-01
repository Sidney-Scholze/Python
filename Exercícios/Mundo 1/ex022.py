nome = str(input('Digite seu nome completo: ')).strip()

print('Em maiusculo {}' .format(nome.upper()))

print('Em minusculo {}'.format(nome.lower()))

print('O nome tem {} letras' .format(len(nome) - nome.count (' ')))

print('O primeiro nome tem {} letras' .format(nome.find(" ")))


#print('O primeiro nome tem: {}' .format(quantos_caracteres_nome1))
