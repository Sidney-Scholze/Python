print('-' *40)
print('Sequencia de Fibonacci')
print('-' *40)
max = int(input('Digite quantos elementos da sequencia de Fibonacci deseja: '))
n = 0
a = 1
b = 0
count = 0
print('{} → Termo 0'.format(n),end= '')
while count < max:

    n = a + b
    a = b
    b = n
    count += 1
    print('\n{} → Termo {}'.format(n, count),end= ' ')
