# 7. Fazer um programa que calcule e imprima a soma de duas matrizes (a ordem das 
# duas matrizes deve ser lida da entrada padrão). 

matrix1 = []
matrix2 = []
print("--------- Cálculo da soma de duas matrizes ---------")

order = 1
while True:
    order = input("Digite a ordem das matrizes: ")
    if order.isnumeric():
        order = int(order)
        break
    continue

for i in range(order):
    column = []
    for j in range(order):
        n = 0
        while True:
            n = input("Digite o valor da posição [{}, {}] da matriz 1: ".format(i, j))
            if str(n).isnumeric():
                break
            continue
        column.append(int(n))
    matrix1.append(column)
    
for i in range(order):
    column = []
    for j in range(order):
        n = 0
        while True:
            n = input("Digite o valor da posição [{}, {}] da matriz 2: ".format(i, j))
            if str(n).isnumeric():
                break
            continue
        column.append(int(n))
    matrix2.append(column)


# Rendering matrix
renderingTemp1 = ''
for i in range(order):
    line = ''
    for j in range(order):
        line += "{} ".format(str(matrix1[i][j]))
    renderingTemp1 += "| {}\n".format(line)

renderingTemp2 = ''
for i in range(order):
    line = ''
    for j in range(order):
        line += "{} ".format(str(matrix2[i][j]))
    renderingTemp2 += "| {}\n".format(line)


resultMatrix = []

for i in range(order):
    column = []
    for j in range(order):
        n = matrix1[i][j] + matrix2[i][j]
        column.append(int(n))
    resultMatrix.append(column)
    
renderingResult = ''
for i in range(order):
    line = ''
    for j in range(order):
        line += "{} ".format(str(resultMatrix[i][j]))
    renderingResult += "| {}\n".format(line)
    
print("""
| Matrix 1
{}
|
| Matrix 2
{}
|
| Matrix Resultante
{}      
      """.format(renderingTemp1, renderingTemp2, renderingResult))