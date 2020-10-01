nome = str(input('Nome e sobrenome: ')).strip()
n = nome.split()
'''
print('Primeiro nome: {} ' .format(n[0]))
print('Ultimo nome: {}' .format(n[len(n) -1 ]))
'''

print('Seu primeiro nome é: {}' .format(n[0]))
print('Seu segundo nome é: {}'.format(n[len(n) -1]))