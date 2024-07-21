def ler_matriz():
    matriz = []
    
    # Pergunta ao usuário quantos elementos cada linha terá
    while True:
        try:
            num_elementos = int(input("Digite o número de elementos por linha: "))
            if num_elementos <= 0:
                print("O número de elementos por linha deve ser maior que zero. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro válido.")
    
    print("Digite as linhas da matriz (pressione Enter em uma linha vazia para terminar):")
    while True:
        linha = input(f"Digite uma linha com {num_elementos} inteiros separados por espaço: ")
        if linha == "":
            break
        
        numeros_str = linha.split()
        
        # Verifica se a quantidade de números na linha está correta
        if len(numeros_str) != num_elementos:
            print(f"A linha deve conter exatamente {num_elementos} números inteiros. Tente novamente.")
            continue
        
        # Verifica se todos os elementos são números inteiros
        if all(num_str.isdigit() or (num_str.startswith('-') and num_str[1:].isdigit()) for num_str in numeros_str):
            numeros = [int(num_str) for num_str in numeros_str]
            matriz.append(numeros)
        else:
            print("A linha deve conter apenas números inteiros. Tente novamente.")
    
    return matriz

def main():
    print("Bem-vindo ao programa de leitura de matriz!")
    matriz = ler_matriz()
    print("\nMatriz lida:")
    for linha in matriz:
        print(" ".join(map(str, linha)))

if __name__ == "__main__":
    main()
