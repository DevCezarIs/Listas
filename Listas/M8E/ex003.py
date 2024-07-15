def calcular_mdc(a, b):
    """Calcula o Máximo Divisor Comum (MDC) de dois números usando o algoritmo de Euclides."""
    while b != 0:
        a, b = b, a % b
    return a

# Exemplo de uso da função
numero1 = int(input())
numero2 = int(input())
resultado = calcular_mdc(numero1, numero2)
print(f"O MDC de {numero1} e {numero2} é: {resultado}")
