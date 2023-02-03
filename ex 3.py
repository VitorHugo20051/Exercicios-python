# verificar se os gastos estão ou não dentro do salário
salario = float(input('Qual é o seu salário? €'))
total_despesas = float(input('Total gastos em despesas: €'))

if salario >= total_despesas:
    print('Gastos dentro do orçamento.')

else:
    print('Orçamento estourado!')