from ex115.lib.interface import *

def leiaInt(n1):

    try:
        nI = int(input(n1))
    except KeyboardInterrupt:
        print('O usuario preferiu não informar o numero')
    except (ValueError,TypeError):
        print('\033[0;31mDigite apenas numero inteiro\033[m')
    else:
        return nI


def linha(tam=40):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for  item in lista:
        print(f'\033[33m{c}\033[m- \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro ao criar arquivo')
    else:
        print('Arquivo criado com sucesso')

def leraquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('erro')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()


def cadastrar(arq,nome = 'Não informado',idade =0):
    try:
        a = open(arq, 'at')
    except:
        print('Hounve um erro')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na gravação dos dados')
        else:
            print('Novo registro adicionado')
            a.close()