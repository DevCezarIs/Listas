# 9. Escreva uma função que dada uma matriz quadrada, verifique se ela é uma matriz 
# triangular superior.

def is_triangular_superior(matrix):
    n = len(matrix)
    # Começa em 1 para não pegar a diagonal principal
    for i in range(1, n):
        for j in range(i):
            
            # Caso queira ver em detalhes, descomente essa seção de prints:

            # print("j: ",j)
            # print("i: ",i)
            # print("matrix[i][j]: ",matrix[i][j])
            # print("-"*15)

            print(matrix)
            if matrix[i][j] != 0:
                return False
                
    return True

# Teste
matriz1 = [
    [1, 2, 3],
    [0, 5, 6],
    [0, 0, 9]
]

matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [0, 0, 9]
]

print(is_triangular_superior(matriz1))
print(is_triangular_superior(matriz2))
