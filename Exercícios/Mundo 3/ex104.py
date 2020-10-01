def leiaInt(put):
    ok = False
    valor = 0
    while True:
        n = str(input(put))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[031mERRO digite apenas numero inteiro\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um numero')
print(f'Voce digitou o numero {n}')
