palavras = ('aprender','programar','linguagem','python',
            'curso', 'gratis','estudar', 'praticar','trabalhar',
            'mercado','programador','futuro')
# a e i o u
vogais = ('a', 'e', 'i', 'o', 'u')
t = 0
for i in palavras:
    print(f'\nVogais de palavra {i}' , end= ' ')
    for letra in i:
        if letra in 'aeiou':
            print(f'{letra.upper()}', end='')
            t += 1
print(f'\nTotal de palavras {len(palavras)}\nTotal de vogais {t}')
