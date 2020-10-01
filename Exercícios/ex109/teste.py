from ex109 import moeda

p = float(input('Digite um preço R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,formatar=False)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,formatar=True)}')
print(f'Aumentando 10% de {moeda.moeda(p)} é {moeda.aumentar(p,10,formatar=False)}')
print(f'Diminuindo 10% de {moeda.moeda(p)} é {moeda.diminuir(p,10,True)}')