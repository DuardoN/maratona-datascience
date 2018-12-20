# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = str(input("Por favor digite seu sexo:\nF - Feminino\nM - Masculino."))

if sexo == 'F':
    print("O sexo é feminino")
elif sexo == 'M':
    print("O sexo é masculino")
else:
    print("Sexo Inválido")