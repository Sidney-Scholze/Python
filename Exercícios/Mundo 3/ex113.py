def leiaInt(n1):

    try:
        nI = int(input(n1))
    except KeyboardInterrupt:
        print('O usuario preferiu não informar o numero')
    except (ValueError,TypeError):
        print('\033[0;31mDigite apenas numero inteiro\033[m')
    else:
        print(f'Voce digitou o numero {nI}')



def leiaFloat(n2):

    try:
        nR = float(input(n2))
    except KeyboardInterrupt:
        print('O usuario preferiu não informar o numero')
    except (ValueError,TypeError):
        print('\033[0;31mDigite apenas numero real\033[m')
    else:
        print(f'Voce digitou o numero {nR}')



while True:
    nI = leiaInt('Digite um numero inteiro: ')
    nR = leiaFloat('Digite um numero real: ')

