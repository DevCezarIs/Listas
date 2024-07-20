"""
13. Uma equação do segundo grau é escrita
ax² + bx + c =
e a sua solução é dada em
função dos valores de a, b e c. Podendo ter duas raízes, uma ou nenhuma. Escreva uma função que resolva a equação do segundo grau, retornando o número de raízes
encontradas. Os valores dessas raízes devem ser retornados em parâmetros.

"""

def resolver_equacao_segundo_grau(a, b, c):
    """Resolve a equação do segundo grau ax^2 + bx + c = 0.
    
    Retorna o número de raízes encontradas e os valores das raízes.
    """
    if a == 0:
        raise ValueError("O valor de 'a' não pode ser 0 em uma equação do segundo grau.")
    
    # Calcula o discriminante
    delta = b**2 - 4*a*c
    
    if delta > 0:
        # Duas raízes reais e distintas
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)
        return 2, raiz1, raiz2
    elif delta == 0:
        # Uma raiz real (raiz dupla)
        raiz = -b / (2*a)
        return 1, raiz
    else:
        # Nenhuma raiz real
        return 0,

def obter_coeficiente(nome):
    """Solicita ao usuário um coeficiente e valida a entrada."""
    while True:
        try:
            valor = float(input(f"Digite o valor de {nome}: "))
            return valor
        except ValueError:
            print(f"Entrada inválida. Por favor, insira um número válido para {nome}.")

def main():
    print("Resolução de equação do segundo grau (ax^2 + bx + c = 0)")
    
    # Solicita os coeficientes ao usuário com validação
    a = obter_coeficiente("a")
    b = obter_coeficiente("b")
    c = obter_coeficiente("c")
    
    # Resolve a equação
    try:
        resultado = resolver_equacao_segundo_grau(a, b, c)
        
        # Exibe os resultados
        num_raizes = resultado[0]
        if num_raizes == 2:
            print(f"A equação tem duas raízes reais: x1 = {resultado[1]}, x2 = {resultado[2]}")
        elif num_raizes == 1:
            print(f"A equação tem uma raiz real: x = {resultado[1]}")
        else:
            print("A equação não tem raízes reais.")
    except ValueError as e:
        print(e)

main()
