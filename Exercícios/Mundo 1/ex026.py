frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} na frase' .format(frase.lower().count('a')))
print('A primeira posição de A é: {} ' .format(frase.lower().find('a')+1))
print('A ultima posição de A é: {}' .format(frase.lower().rfind('a')+1))