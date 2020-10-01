from datetime import date
print('Considerando que você não se alistou ao exercito')
idade = int(input('Qual sual idade: '))
data_ = (date.today().year - idade) +18

if date.today().year == data_:
    print('Se ainda não se apresentou, este ano você deve se apresentar')
elif date.today().year > data_:
    print('Você deveria ter se apresentado hà {} anos '.format(date.today().year - data_ ))
    print('Seu alistamento foi em {}' .format(data_))
elif date.today().year < data_:
    print('Faltam {} anos para você se apresentar' .format(data_ - date.today().year ))

