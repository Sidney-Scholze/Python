Total = ProdutosAcima1000 = ProdutoBarato = Count = 0
Nome = ''
print('='*50)
print('Loja 1')
print('='*50)
while True:

    Sair = ' '
    Produto = str(input('Produto: '))
    Preço = float(input('Preço: R$'))
    Count +=1
    Total += Preço
    if Preço > 1000:
        ProdutosAcima1000 +=1
    if Count == 1 or Preço < ProdutoBarato :
        ProdutoBarato = Preço
        Nome = Produto

    while Sair not in 'SN':
        Sair = str(input('Deseja encerrar ? [S/N]')).strip().upper()
    if Sair == 'S':
        break
print('{:-^40}'.format('Fim'))
print('O total da compra foi R$: {:.2f}'.format(Total))
print('{} produtos custam mais de R$ 1000.00'.format(ProdutosAcima1000))
print('O produto mais barato foi: {} e custou R$ {:.2f}'.format(Nome, ProdutoBarato))
