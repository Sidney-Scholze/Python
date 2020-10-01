def metade(p, formatar=False):
    resp = p / 2
    return resp if formatar is False else moeda(resp)


def dobro(p, formatar=False):
    resp = p * 2
    return resp if formatar is False else moeda(resp)


def aumentar(p,taxa, formatar=False):
    resp = p + (p * taxa /100)
    return resp if formatar is False else moeda(resp)


def diminuir(p,taxa, formatar=False):
    resp = p - (p *taxa) /100
    return resp if formatar is False else moeda(resp)


def moeda(p=0, moeda='R$'):
    return f' {moeda}{p:.2f}'.replace('.',',')