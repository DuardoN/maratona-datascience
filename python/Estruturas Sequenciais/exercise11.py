# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a - o produto do dobro do primeiro com metade do segundo.
# b - a soma do triplo do primeiro com o terceiro.
# c - o terceiro elevado ao cubo.
numero1 = int(input('Por favor digite um numero inteiro: '))
numero2 = int(input('Por favor digite outro numero inteiro: '))
numero3 = float(input('Por favor digite um numero real: '))

dobro_numero1 = numero1*2
a = (dobro_numero1 ** 2) + (numero2 ** 0.5)

triplo_numero1 = float(float(numero1)*3)
b = triplo_numero1 + numero3

c = (numero3 ** 3)