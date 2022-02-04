# Exercicio 01 - Aula 01

# Faça um programa que peça um valor monetário e diminua-o em 15%. Seu 
# programa deve imprimir a mensagem “O novo valor é [valor]”.

salario = int(input("Digite seu salário: "))
desconto = ((salario * 15)/100)
saldo = salario - desconto

print("Seu salário com desconto é: ", saldo)
