from time import sleep


def maior(*num):
    print('=-' * 50)
    print('\nAnalisando...', flush=True)
    n_maior = max(num)
    for n in num:
        print(f'{n}', end=' ')
        sleep(1)
    print(f'\nForam informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {n_maior}')


maior(1, 2, 7, 4, 6)
maior(9, 7, 0, 10, 1, 22)
maior(0)
