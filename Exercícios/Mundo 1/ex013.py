titulo = ('Aumento de salario')
print('\n{:>50}'.format(titulo))
salario_a = float(input('Salario Atual: '))
salario_b = salario_a + (15 * salario_a) / 100
print('Salario com 15% de aumento: {}' .format(salario_b))