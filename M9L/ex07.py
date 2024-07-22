'''
7. Escreva uma função que dada uma matriz quadrada, verifique se ela é uma matriz
diagonal.

'''

def ler_ordem_matriz_quadrada():
    while True:
        ordem = input("Digite a ordem da matriz quadrada (número de linhas e colunas): ").strip()
        if ordem.isdigit() and int(ordem) > 0:
            return int(ordem)
        else:
            print("Entrada inválida. A ordem da matriz deve ser um número inteiro positivo.")

def ler_matriz_quadrada(ordem):
    matriz = []
    
    print("Digite as linhas da matriz:")
    while len(matriz) < ordem:
        linha = input(f"Digite uma linha com {ordem} inteiros separados por espaço: ").strip()
        if linha == "":
            print("A matriz precisa ter exatamente a ordem especificada. Tente novamente.")
            continue
        
        numeros_str = linha.split()
        
        # Verifica se a quantidade de números na linha está correta
        if len(numeros_str) != ordem:
            print(f"A linha deve conter exatamente {ordem} números inteiros. Tente novamente.")
            continue
        
        # Verifica se todos os elementos são números inteiros
        try:
            numeros = [int(num_str) for num_str in numeros_str]
            matriz.append(numeros)
        except ValueError:
            print("A linha deve conter apenas números inteiros. Tente novamente.")
    
    return matriz

def verifica_matriz_diagonal(matriz):
    ordem = len(matriz)
    
    for i in range(ordem):
        for j in range(ordem):
            if i != j and matriz[i][j] != 0:
                return False
    return True

def main():
    print("Bem-vindo ao programa de leitura de matriz quadrada!")
    print(
        '''
        Exemplo de matriz diagonal:
                [1, 0, 0]
                [0, 1, 0]
                [0, 0, 1]
        '''
    )
    ordem = ler_ordem_matriz_quadrada()
    matriz = ler_matriz_quadrada(ordem)
    
    print("\nMatriz lida:")
    for linha in matriz:
        print(" ".join(map(str, linha)))
    
    if verifica_matriz_diagonal(matriz):
        print("\nA matriz é uma matriz diagonal.")
    else:
        print("\nA matriz não é uma matriz diagonal.")

main()
