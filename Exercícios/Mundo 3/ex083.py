lista = input('Digite a expressão: ').strip()
p =0
for pos, v in enumerate(lista):
    if '(' == v:
        p += 1
    if ')' == v:
        p -= 1
    if p == 0:
        res = 'Correta!'
    else:
        res = 'incorreta'
print(f'Sua expressão está {res}')
