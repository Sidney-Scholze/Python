while True:
    num = int(input('\nQuer ver a tabuada de qual valor?: '))
    if num < 0:
        print('Fim:')
        break
    for count in range (1,11):
    # tabuada = num * count
         print('{} X {} = {}' .format(num, count ,num * count))
     #count = 0

