frase = str(input('Veja se uma frase é políndromo: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso =''
for letras in range(len(junto) -1,-1,-1):
    inverso += junto[letras]
if inverso == junto:
    print('{} é um palíndromo'.format(junto))
else:
    print('{} não é um palíndromo'.format(inverso))

