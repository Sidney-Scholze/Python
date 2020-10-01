from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'Menor = {min(a)}')
print(f'Maior = {max(a)}')
