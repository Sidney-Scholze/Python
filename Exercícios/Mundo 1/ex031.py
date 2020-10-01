dist = (float(input('Qual a distância da viagem ?: ')))
print('Viagens de até 200Km custam  R$0.50 por Km\nPara viagens mais longas custam R$0.45 por Km')
if dist >= 200:
    print('O valor da passagem custa: R${:.2f}' .format(dist * 0.45))
else:
    print('O valor da passagem custa: R${:.2f}' .format(dist * 0.50))

