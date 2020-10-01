resutado = 0
opção = 0
val1 = float(input('Valor 1: '))
val2 = float(input('Valor 2: '))

while opção != 5:
    print('[1]Somar\n[2]Multiplicar\n[3]Maior numero\n[4]Novos números\n[5]Sair')
    opção = int(input('Opções: '))


    if opção == 1:

      resultado = val1 + val2
      print(resultado)
    elif opção == 2:
      resultado = val1 * val2
      print(resultado)
    elif opção == 3:
        if val1 > val2:
            resultado = val1
            print(resultado)
        else:
            resultado = val2
            print(resultado)
    elif opção == 4:
        print('[1]Somar\n[2]Multiplicar\n[3]Maior numero\n[4]Novos números\n[5]Sair')

        val1 = float(input('Valor 1: '))
        val2 = float(input('Valor 2: '))
    elif opção == 5:
        print('finalizando')











