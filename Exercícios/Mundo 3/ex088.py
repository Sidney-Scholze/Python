from random import randint
from time import sleep
mega = list()
temp = list()
Qjogos = 0
print('='*30)
print(f'JOGO DA MEGA')
print('='*30)
Qjogos = int(input(f'Quantos jogos quer que eu sorteie: '))
while True:
     n_ran = randint(1,60)
     if n_ran not in temp:
      temp.append(n_ran)
      while len(temp) == 6:
       mega.append(temp[:])
       temp.clear()
      if Qjogos == len(mega):
          break
for Qjogos in range(0,len(mega)):
    sleep(1)
    print(f'Jogo {Qjogos +1}: {mega[Qjogos]}', sep='  ')
