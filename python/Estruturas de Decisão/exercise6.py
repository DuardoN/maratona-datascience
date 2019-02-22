# Faça um Programa que leia três números e mostre o maior deles.
numero1 = float(input("Digite numero um: "))
numero2 = float(input("Digite numero doi: "))
numero3 = float(input("Digite numero tres: "))

maior = numero1

if numero2 < numero1 and numero2 < numero3:
    maior = numero2
if numero3 < numero1 and numero3 < numero2:
    maior = numero3

print(maior)