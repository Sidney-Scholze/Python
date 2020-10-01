print('Calculo tinta necessaria para uma parede')
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
print('Sabendo que 1 litro cobre 2 metros quadrados')
Area_parede = largura * altura
print('Area da parede: {:.2f}²\nÉ necessario: {:.3f} litro(s) de tinta para essa parede' .format(Area_parede,Area_parede / 2))