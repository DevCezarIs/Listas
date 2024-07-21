'''Uma matriz quadrada de números inteiros é um quadrado mágico se o valor da soma
dos elementos de cada linha, de cada coluna e da diagonal principal e da diagonal
secundária é o mesmo. Além disso, a matriz deve conter todos os números inteiros
do intervalo [1..n * n]. Escreva um programa que, dada uma matriz quadrada,
verifique se ela é um quadrado mágico.
'''

def ler_matriz_quadrada():
    matriz = []
    
    # Pergunta ao usuário a ordem da matriz quadrada
    ordem = input("Digite a ordem da matriz quadrada (número de linhas e colunas): ")
    while not (ordem.isdigit() and int(ordem) > 0):
        print("Entrada inválida. A ordem da matriz deve ser um número inteiro positivo.")
        ordem = input("Digite a ordem da matriz quadrada (número de linhas e colunas): ")
    
    ordem = int(ordem)
    
    print("Digite as linhas da matriz (pressione Enter em uma linha vazia para terminar):")
    while len(matriz) < ordem:
        linha = input(f"Digite uma linha com {ordem} inteiros separados por espaço: ")
        if linha == "":
            print("A matriz precisa ter exatamente a ordem especificada. Tente novamente.")
            continue
        
        numeros_str = linha.split()
        
        # Verifica se a quantidade de números na linha está correta
        if len(numeros_str) != ordem:
            print(f"A linha deve conter exatamente {ordem} números inteiros. Tente novamente.")
            continue
        
        # Verifica se todos os elementos são números inteiros
        if all(num_str.lstrip('-').isdigit() for num_str in numeros_str):
            numeros = [int(num_str) for num_str in numeros_str]
            matriz.append(numeros)
        else:
            print("A linha deve conter apenas números inteiros. Tente novamente.")
    
    return matriz

def eh_quadrado_magico(matriz):
    ordem = len(matriz)
    soma_linhas = sum(matriz[0])
    
    # Verifica se a matriz contém todos os números de 1 a n^2
    todos_numeros = set(range(1, ordem * ordem + 1))
    numeros_matriz = set(num for linha in matriz for num in linha)
    if todos_numeros != numeros_matriz:
        return False
    
    # Verifica somas das linhas
    for linha in matriz:
        if sum(linha) != soma_linhas:
            return False
    
    # Verifica somas das colunas
    for j in range(ordem):
        if sum(matriz[i][j] for i in range(ordem)) != soma_linhas:
            return False
    
    # Verifica soma da diagonal principal
    if sum(matriz[i][i] for i in range(ordem)) != soma_linhas:
        return False
    
    # Verifica soma da diagonal secundária
    if sum(matriz[i][ordem - 1 - i] for i in range(ordem)) != soma_linhas:
        return False
    
    return True

def main():
    print("Bem-vindo ao programa de verificação de quadrado mágico!")
    matriz = ler_matriz_quadrada()
    print("\nMatriz lida:")
    for linha in matriz:
        print(" ".join(map(str, linha)))
    
    if eh_quadrado_magico(matriz):
        print("\nA matriz é um quadrado mágico.")
    else:
        print("\nA matriz não é um quadrado mágico.")

main()