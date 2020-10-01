valor_normal =float(input('\nValor do produto: '))

print('\nCondição de pagamento \n')
print('1 para a vista em dinheiro com 10& de desconto')
print('2 para a vista no catão com 5% de desconto')
print('3 Em até 2x no cartão com preço normal')
print('4 3x ou mais no cartão com 20% de juros')

condição_pagamento = int(input('Opção: '))

if condição_pagamento == 1:
    print('O produto de R${:.2f} fica por R${:.2f}'.format(valor_normal,valor_normal -(10 * valor_normal)/100))
elif condição_pagamento == 2:
    print('O produto de R${:.2f} fica por R${:.2f}' .format(valor_normal,valor_normal-(5 * valor_normal)/100))
elif condição_pagamento == 3:
    print('Valor normal de R${:.2f}'.format(valor_normal))
elif condição_pagamento == 4:
    print('Preço normal de R${:.2f} fica por R${:.2f} com 20% de juros' .format(valor_normal, valor_normal + (20 * valor_normal)/100))
else:
    print('Opção invalida')

