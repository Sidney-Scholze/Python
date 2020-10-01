num = int(input('numero: '))
#print('Resto = {}'.format(num / num))
total =0
for c in range (1 , num +1):
    if num % c == 0:
     
        total += 1
if total == 2:
    print('{} é numero primo'.format(c))
else:
    print('{} não é um numero primo'.format(c))

