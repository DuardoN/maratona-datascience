# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a - salário bruto.
# b - quanto pagou ao INSS.
# c - quanto pagou ao sindicato.
# d - o salário líquido.
# e - calcule os descontos e o salário líquido, conforme a tabela abaixo:
#   + Salário Bruto : R$
#   - IR (11%) : R$
#   - INSS (8%) : R$
#   - Sindicato ( 5%) : R$
#   = Salário Liquido : R$
valor_hora = float(input('Quanto você ganha por hora: '))
horas_mes = float(input('Quantas horas você trabalho no mês: '))
salario_mes = valor_hora * horas_mes
print('Você ganha de salario bruto R$', salario_mes, 'por mês')

ir = salario_mes * (11/100)
print('Você paga de IR R$', ir, 'por mês')

inss = salario_mes * (8/100)
print('Você paga de INSS R$', inss, 'por mês')

sindicato = salario_mes * (5/100)
print('Você paga de Sindicato R$', sindicato, 'por mês')

salario_liquido = salario_mes - sindicato - inss - ir
print('Ganha de salario liquido R$', salario_liquido, 'por mês')