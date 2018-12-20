# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input("Por favor digite uma letra: "))

if (letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'i') or (letra == 'o') or (letra == 'u'):
    print('Essa letra é uma vogal.')
else:
    print('Essa letra é uma consoante.')


# outra forma de ser feita
letra = str(input("Por favor digite uma letra: "))
vogais = ['a', 'e', 'i', 'o', 'u']

if letra in vogais:
    print('Essa letra é uma vogal.')
else:
    print('Essa letra é uma consoante.')