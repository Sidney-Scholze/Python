import math
Angulo = float(input('Digite um angulo em graus: '))
Seno = math.sin(math.radians(Angulo))
Cosseno = math.cos(math.radians(Angulo))
Tangente = math.tan(math.radians(Angulo))
print(' O Seno de {:.2f} é {:.2f}\n O Cosseno é {:.2f}\n A Tangente é {:.2f}'.format(Angulo,Seno,Cosseno,Tangente))
