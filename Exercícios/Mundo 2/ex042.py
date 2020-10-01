print('\nTriângulo v2.0')
r1 = float(input('Segmento A:'))
r2 = float(input('Segmento B:'))
r3 = float(input('Segmento C:'))

if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo',end =' ')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 != r3 !=r1:
        print('Escaleno')
    else:
        print('Isósceles')
else: print('Os segmentos não podem formar um triãngulo ')