from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    resposta = menu(['Ver Pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resposta == 1:
        # opção de lista conteudo do arquivo
        leraquivo(arq)
    elif resposta == 2:
        # Cadastra nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = leiaInt('IDADE: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('Digite uma opção válida')