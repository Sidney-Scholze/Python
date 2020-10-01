c ={'\033[m',
      '\033[0;30;44m'}
def ajuda(comando):
    print('\033[7;30m', end='')
    help(comando)



def titulo(msg,cor=0):
   tam = len(msg)
   print('\033[0;30;44m',end='')
   print('-' * tam)
   print(msg)
   print('-' * tam)
   print('\033[m')

while True:
    titulo('SISTEMA DE AJUDA PyHELP',cor=1)
    comando = str(input('Função ou Biblioteca>'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)