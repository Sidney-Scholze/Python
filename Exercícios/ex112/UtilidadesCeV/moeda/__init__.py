def metade(p):
    resp = p / 2
    return moeda(resp)


def dobro(p):
    resp = p * 2
    return moeda(resp)


def aumentar(p,porcmaior):
    resp = p + (p * porcmaior /100)
    return moeda(resp)


def diminuir(p,porcmenor):
    resp = p - (p *porcmenor) /100
    return moeda(resp)


def moeda(p=0, moeda='R$'):
    return f' {moeda}{p:.2f}'.replace('.',',')


def resumo(p,porcmaior, porcmenor):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado \t{(moeda(p))}')
    print(f'Dobro do preço \t\t{(dobro(p))}')
    print(f'Metade do preço \t{metade(p)}')
    print(f'{porcmaior}% de aumento \t{aumentar(p,porcmaior)}')
    print(f'{porcmenor}% de redução \t\t{diminuir(p,porcmenor)}')
    print('-' * 30)