number = int(input('Escreva um numero inteiro: '))
print('Escolha uma das opções:')
bin = bin(number)
oct = oct(number)
hex = hex(number)
print('''
[B] para converter para binário
[O] para converter Octal
[H] para converter hexadecimal''')
dig = str(input('\nOpção: ')).strip().upper()

if dig == 'B':
    print('{} -> {}'.format(number,bin[2:]))
elif dig == 'O':
    print('{} -> {}'.format(number,oct[2:]))
elif dig == 'H':
    print('{} -> {}' .format(number,hex[2:].upper()))
