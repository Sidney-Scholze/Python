Velocidade = float(input('Velocidade do carro: '))

v_superior = (Velocidade - 80) * 7
cores = {'Limpa': '\033[m' ,
         'Vermelho':'\033[0;31m',
         'Verde':'\033[7;32m',
         'PB':'\033[7;30m'}
print('{}---Limite de velocidade = 80km/h---{}' .format(cores['PB'] , cores['Limpa']))
if Velocidade > 80:
    print('{}{}Km/h voce ultrupassou {}Km/h' .format(cores['Vermelho'],Velocidade,Velocidade - 80 ,end = ' '))
    print('A multa custa R$ 7.00 reais por km/h acima do permitido\nA multa vai custar R${:.2f}' .format(v_superior))
else:
    print('{}Continue dentro do limite de velocidade {}'.format(cores['Verde'],cores['Limpa']))