def metade(p):
    resp = p / 2
    return resp


def dobro(p):
    resp = p * 2
    return resp


def aumentar(p,taxa):
    resp = p + (p * taxa /100)
    return resp


def diminuir(p,taxa):
    resp = p - (p *taxa) /100
    return resp


def moeda(preço=0, moeda='R$'):
    return f' {moeda}{preço:.2f}'.replace('.',',')