t = 0
s = 0
for n in range (1,501,2):

      if n % 3 == 0:
        t += n
        s += 1
print('A soma dos multiplos de 3 = {}\nTotal de multiplos = {}'.format(t,s))