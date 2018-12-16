# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input('Por favor digite sua altura: '))
peso_ideal_homem = (72.7*h) - 58
peso_ideal_mulher = (62.1*h) - 44.7
print('Caso você seja homem seu peso ideal seria: ', peso_ideal_homem)
print('Caso você seja mulher seu peso ideal seria: ', peso_ideal_mulher)