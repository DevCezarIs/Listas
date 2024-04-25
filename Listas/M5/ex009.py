# 9. Fazer um programa que calcule e imprima o produto por um escalar de uma matriz 
# qualquer com dimensões máximas de 20x20. 

matrix = []
print("--------- Cálculo da soma de duas matrizes ---------")

order = 1
while True:
    order = input("Digite a ordem das matrizes (máximo de 20): ")
    if order.isnumeric():
        order = int(order)
        break
    continue

if order > 20:
    order = 20

for i in range(order):
    column = []
    for j in range(order):
        n = 0
        while True:
            n = input("Digite o valor da posição [{}, {}] da matriz: ".format(i, j))
            if str(n).isnumeric():
                break
            continue
        column.append(int(n))
    matrix.append(column)

while True:
    escalar = input("Digite o valor escalar a ser multiplicado pela matriz: ")
    if escalar.isnumeric():
        escalar = int(escalar)
        break
    continue

# Rendenring result before change values

renderingTemp = ''
for i in range(order):
    line = ''
    for j in range(order):
        line += "{} ".format(str(matrix[i][j]))
    renderingTemp += "| {}\n".format(line)

# Changing values

for i in range(order):
    for j in range(order):
        matrix[i][j] = matrix[i][j] * escalar


# Rendering result matrix
    
renderingResult = ''
for i in range(order):
    line = ''
    for j in range(order):
        line += "{} ".format(str(matrix[i][j]))
    renderingResult += "| {}\n".format(line)
    
print("""
| Matriz original:
{}
| Escalar: {}

| Matriz resultante:
{}
      """.format(renderingTemp, escalar, renderingResult))