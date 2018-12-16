# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.
peso_estabelecido = 50.00
multa_peso_excedente = 4.00
peso_peixes = float(input('Peso peixe pescado: '))

excesso = peso_peixes - peso_estabelecido
multa = excesso * multa_peso_excedente

print('João tera que pagar R$', multa, 'de multa.\nSe o valor for negativo, joão não precisara pagar multa')