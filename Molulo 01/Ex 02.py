# Exercicio 02 - Aula 01

# Faça um programa que leia a validade das informações:
# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, F ou Outro;
# O programa deve imprimir uma mensagem de erro para cada informação 
# inválida.

idade = int(input("Digite sua idade entre 0 à 150: "))
if 0 < idade < 150:
    print("Ok"),
else:
    print("Erro, idade não aceita")

salario = int(input("Digite seu salário maior que 0: "))
if salario > 0:
    print("Ok")
else:
    print("Erro, salário igual a 0")

sexo = input("Digite (M)asculino, (F)eminino ou (O)utro: ").upper()
if sexo == "M" or sexo == "F" or sexo == "O":
    print("Ok")
else:
    print("Erro, aceito somente M, F ou O")
