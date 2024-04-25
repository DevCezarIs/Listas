# 15. Elabore um programa que calcule e mostre a soma dos 10 primeiros termos da série:
# Fração x/y, onde x é um número que começa em 100 e decresce, e y é o fatorial de um número crescente iniciado em 0.

many = 10

fatorialTemp = 1

for i in range(0, 100, 1):
    if (many <= 0):
        break
    if (i == 0):
        print("{}° termo: {}".format((i + 1), (100 - i)/fatorialTemp))
        continue
    fatorialTemp *= i
    print("{}° termo: {}".format((i + 1), (100 - i)/(fatorialTemp)))
    # print("Fatorial de {} é {}".format(i, fatorialTemp))
    
    many -= 1