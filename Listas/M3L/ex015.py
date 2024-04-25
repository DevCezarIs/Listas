# 15. Construa um programa que receba três valores quaisquer e imprima-os em ordem 
# crescente. Como seu programa reage a valores de entrada iguais como no exercício 
# anterior?

numeros = [0, 0, 0]

n1 = int(input("(1°) Digite um número inteiro: "))
n2 = int(input("(2°) Digite um número inteiro: "))
n3 = int(input("(3°) Digite um número inteiro: "))

first = 0
mid = 0
last = 0

# Encontrando o menor valor

if(n1 <= n2 and n1 <= n3):
    numeros[0] = n1
    first = 1
elif(n2 <= n1 and n1 <= n3):
    numeros[0] = n2
    first = 2
elif(n3 <= n1 and n3 <= n2):
    numeros[0] = n3
    first = 3

# Encontrando o maior valor

if(n1 >= n2 and n1 >= n3):
    numeros[2] = n1
    last = 1
elif(n2 >= n1 and n1 >= n3):
    numeros[2] = n2
    last = 2
elif(n3 >= n1 and n3 >= n2):
    numeros[2] = n3
    last = 3

if(first != 1 and last != 1):
    mid = 1
    numeros[1] = n1
elif(first != 2 and last != 2):
    mid = 2
    numeros[1] = n2
elif(first != 3 and last != 3):
    mid = 3
    numeros[1] = n3
else:
    print("Ops, algo deu errado...")

print("A ordem crescente dos números escolhidos é {}, {} e {}.".format(numeros[0], numeros[1], numeros[2]))