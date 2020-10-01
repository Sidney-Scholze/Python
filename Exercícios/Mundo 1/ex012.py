titulo = ('Porcentagem')
print('\n{:=^60}' .format(titulo))
valor_produto = float(input('Valor do produto sem desconto: '))
valor_desconto = valor_produto - (5 * valor_produto) / 100
print('Produto sem desconto: {:.2f}\nProduto com 5% de desconto: {:.2f}' .format(valor_produto,valor_desconto))
