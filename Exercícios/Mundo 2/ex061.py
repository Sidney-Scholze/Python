print('*'*50)
print('Progressão Aritimetica com While P.A')
print('*'*50)
termo = int(input('Termo: '))
razao = int(input('Razão: '))
quantum_t = 10
count = 0
while  0 < quantum_t:
    print('{}'.format(termo), end=' ')
    termo  += razao
    quantum_t -= 1
    count += 1
    if 0 == quantum_t:
        quantum_t = int(input('\nDeseja ver mais quantos termos?[0]Para Sair'))
print('Termos Analisados {}'.format(count))
