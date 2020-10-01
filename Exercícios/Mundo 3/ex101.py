


def voto(ano):
    from datetime import date
    idade = date.today().year - ano

    if idade < 18:
        return f'Com {idade} anos você ainda não vota'
    elif 65 >= idade >= 18:
        return f'Com {idade} anos seu voto é obrigatorio'
    elif 65 < idade:
        return f'Com {idade} anos seu voto é opcional'



ano_nascimento = int(input('Digite seu ano de nascimento: '))
print(voto(ano_nascimento))

