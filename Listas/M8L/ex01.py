def mdc(a, b):
    """Calcula o Máximo Divisor Comum (MDC) usando o algoritmo de Euclides."""
    while b != 0:
        a, b = b, a % b
    return a

def mdc_lista(lista):
    """Calcula o MDC de uma lista de três ou mais números inteiros positivos."""
    if len(lista) < 2:
        print("A lista deve conter pelo menos dois números")
        return None

    resultado = lista[0]
    for num in lista[1:]:
        resultado = mdc(resultado, num)
    return resultado

def solicitar_numeros():
    #Solicita números inteiros positivos ao usuário e trata possíveis erros de entrada.
    while True:
        try: #Pede para o usuario já suspeitando de erros 
            numeros = input("Digite uma lista de números inteiros positivos separados por espaço: ").split()
            numeros = [int(num) for num in numeros if int(num) > 0]
            if len(numeros) < 2:
                print("Por favor, digite pelo menos dois números inteiros positivos.")
            else:
                return numeros
        except ValueError: #Em caso de erros, o except evita que o programa pare
            print("Entrada inválida. Certifique-se de digitar apenas números inteiros positivos.")

def testar_funcoes():
    """Função para testar as funções mdc e mdc_lista."""
    print("\n--- Testando Funções MDC ---")
    # Solicitando números ao usuário e calculando o MDC da lista
    numeros_usuario = solicitar_numeros()
    mdc_resultado = mdc_lista(numeros_usuario)
    
    print("\n--- Resultado ---")
    if mdc_resultado is not None:
        print(f"MDC da lista digitada pelo usuário {numeros_usuario}: {mdc_resultado}")
    else:
        print("Não foi possível calcular o MDC devido a entradas inválidas.")
    
    print("\n--- Fim dos Testes ---")

# Testar as funções
testar_funcoes()