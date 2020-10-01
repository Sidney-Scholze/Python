tupla = ('Lápis', 1.75, 'Borracha', 2.00,'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas' , 22.30, 'Livro', 34.90)
print(f'-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print(f'-' * 50)
for c in range (0,len(tupla),2):
    print(f'{tupla[c]:.<35}R${tupla[c + 1]:>7.2f}')
print(f'-' * 50)
