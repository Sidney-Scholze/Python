import time


def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'De {i} até {f} em passo de {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont -= p
    print()



contador(1,10,1)
contador(10,0,2)
ini = int(input('Valor de start: '))
fim = int(input('Valor de stop: '))
pas = int(input('Valor de passo: '))
contador(ini,fim,pas)