import math
import time
def fatorial(num,show=False):
    """
    Calcula o Fatorial de um numero
    :param num: O numero a ser calculado
    :param show: Opcional para mostrar o calculo
    :return:
    """

    f = 1

    for c in range(num,0,-1):


        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print(f'x',end=' ')
            else:
                print(f'=',end=' ')
        f *= c

    return f


#n = int(input('Informe numero para calculo de seu fatorial: '))

print(fatorial(5,show=True))
#help(fatorial)




