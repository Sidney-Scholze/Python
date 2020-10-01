
def notas(*notas,sit=False):
    """
    Função para analisar notas de alunos
    :param notas: Todas as notas do aluno
    :param sit: sit > 7.0 é bom, sit < 7 não é bom
    :return: Retorna o valor do dicionario
    """
    dic = {'Total':len(notas),'Maior': max(notas),'Menor':min(notas),'Média':sum(notas) / len(notas)}

    if sit:
        if dic["Média"] >= 7:
            dic["Situação"] = 'Muito Bom!'
        else:
            dic["Situação"] = 'Precisa se esforçar'

    return dic


resp = (notas(5.5, 9.5, 1, 6.5,sit=True))
print(resp)
