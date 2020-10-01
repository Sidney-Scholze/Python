print('Tabuada')
num = int(input('Digite um numero para ver sua tabuada: '))

for count in range(1,11,1):
    print('{} x {} = {}' .format(num,count, num * count))