print('Media de notas')
nota1 = float(input('Primeira nota: '))
nota2 = float(input(('Segunda nota: ')))
média = (nota1 + nota2)/2

if média < 5.0:
    print('Reprovado sua média é: {:.1f}' .format(média))
elif  7 > média > 5.0:
    print('Vai ficar em recuperação sua média é {:.1f}'.format(média))
elif média > 7:
    print('Aprovado sua média foi: {:.1f}' .format(média))