# Vamos fazer um programa para verificar quem é o assassino de um crime.
# Para descobrir o assassino, a polícia faz um pequeno questionário com 5
# perguntas onde a resposta só pode ser sim ou não:
# a. Mora perto da vítima?
# b. Já trabalhou com a vítima?
# c. Telefonou para a vítima?
# d. Esteve no local do crime?
# e. Devia para a vítima?
# Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
# suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
# 2 pontos são apenas suspeitos, necessitando outras investigações. Valores
# iguais ou abaixo de 1 são liberados.

from re import S

suspeito = 0
a = input("Mora perto da vítuma? (S)im ou (N)ão: ").upper()
if a == "S":
    suspeito = suspeito + 1
else:
    suspeito = suspeito + 0

b = input("Já trabalhou com a vítima? (S)im ou (N)ão: ").upper()
if b == "S":
    suspeito = suspeito + 1
else:
    suspeito = suspeito + 0

c = input("Telefonou para a vítima? (S)im ou (N)ão: ").upper()
if c == "S":
    suspeito = suspeito + 1
else:
    suspeito = suspeito + 0

d = input("Esteve no local do crime? (S)im ou (N)ão: ").upper()
if d == "S":
    suspeito = suspeito + 1
else:
    suspeito = suspeito + 0

e = input("Devia para a vítima? (S)im ou (N)ão: ").upper()
if e == "S":
    suspeito = suspeito + 1
else:
    suspeito = suspeito + 0


