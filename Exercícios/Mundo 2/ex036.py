print('\n\033[1;1mEmprestimo Bancario')
valor_casa = float(input('Qual o valor da casa:'))
salario = float(input(('Qual seu salário:')))
prestação_anual = float(input('Em quantos anos deseja pagar:'))

prestação_mensal = (valor_casa / prestação_anual) / 12
percentual_do_salario = (30 * salario)/100
print('A prestação mensal fica em R${:.2f}'.format(prestação_mensal))
if prestação_mensal > percentual_do_salario:
    print('EMPRESTIMO NEGADO - Sua prestação mensal ultrapassa 30% do seu salário')
elif prestação_mensal < percentual_do_salario:
    print('EMPRESTISMO APROVADO !')
