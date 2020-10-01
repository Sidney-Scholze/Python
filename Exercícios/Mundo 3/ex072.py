numeros = ('Zero','Um','Dois','Tres','quatro','cinco',
           'seis','sete','oito','nove','dez',
           'onze', 'doze','treze','quatorze','quinze',
           'desesseis','dezesete','dezoito','dezenove','vinte')

while True:
    n = int(input('Escolha um numero entre 0 e 20: '))
    if 0 <= n <= 20:
      print(numeros[n])
    else:
        print('Digite um numero valido')
