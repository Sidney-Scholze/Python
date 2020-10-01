print('\n\033[1;31mÍndice de massa corporal IMC\033[m')
altura = float(input('Qual sua altura ?: '))
peso = float(input('Qual o seu peso ?: '))
imc = peso / altura ** 2
while True:
    if imc < 18.5:
        print('Abaixo do peso')
    elif imc > 18.5 and imc < 25:
        print('Peso ideal')
    elif imc > 25 and imc <= 30:
        print('Sobrepeso')
    elif imc > 30 and imc <= 40:
        print('Obesidade')
    elif imc > 40:
        print('Obesidade mórbida')

    print('Seu IMC é: {:.2f}'.format(imc))
    break
