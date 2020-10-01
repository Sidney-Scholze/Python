times = ('Corinthians', 'Palmeiras', 'Santos','Gremio',
         'Cruzeiro','Flamengo','Vasco','Chapecoense',
         'Atletico','Botago','Atletico-PR','Bahia',
         'Sao Paulo','Fluminense','Sport Recife',
         'EC Vitoria','Curitiba','Avaí','Ponte Preta',
         'Atletico-GO')
print('Lista de times {}'.format(times))
print('Os cinco primeiros são {}'.format(times[:5]))
print('OS quatro ultimos colocados {}'.format(times[16:20]))
print('Times em ordem alfabetica: {}'.format(sorted(times)))
print('O Chapecoense está na {} posição'.format(times.index('Chapecoense')+1))