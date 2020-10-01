salario = float(input('Qual o salario do funcionario: '))
if salario <= 1250.00:
    print('O aumento de salario será de 15% : {:.2f}' .format(salario + (15 * salario) / 100))
else:
    print('O aumento de salario será de 10%   {:.2f}' .format(salario +(10 *(salario)/100)))