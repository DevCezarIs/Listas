"""
Escreva as seguintes funções:
a. CparaF - faz a conversão de uma temperatura em graus C para graus F.
b. CparaK - faz a conversão de uma temperatura em C para Kelvin (C=K-273)
c. KparaC - faz a conversão de K para C.
d. KparaF - faz a conversão de K para F (dica: utilize as funções anteriores)
e. FparaK - faz a conversão de F para K. 

"""

def CparaF(celsius):
    """Converte Celsius para Fahrenheit"""
    return (9/5) * celsius + 32

def CparaK(celsius):
    """Converte Celsius para Kelvin"""
    return celsius + 273.15

def KparaC(kelvin):
    """Converte Kelvin para Celsius"""
    return kelvin - 273.15

def KparaF(kelvin):
    """Converte Kelvin para Fahrenheit"""
    # Primeiro, converte Kelvin para Celsius
    celsius = KparaC(kelvin)
    # Depois, converte Celsius para Fahrenheit
    return CparaF(celsius)

def FparaK(fahrenheit):
    """Converte Fahrenheit para Kelvin"""
    # Primeiro, converte Fahrenheit para Celsius
    celsius = (fahrenheit - 32) * 5/9
    # Depois, converte Celsius para Kelvin
    return CparaK(celsius)

def FparaC(fahrenheit):
    """Converte Fahrenheit para Celsius"""
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print("\nEscolha a conversão de temperatura:")
        print("1. Celsius para Fahrenheit (CparaF)")
        print("2. Celsius para Kelvin (CparaK)")
        print("3. Kelvin para Celsius (KparaC)")
        print("4. Kelvin para Fahrenheit (KparaF)")
        print("5. Fahrenheit para Kelvin (FparaK)")
        print("6. Fahrenheit para Celsius (FparaC)")
        print("7. Sair")

        escolha = input("\nDigite o número da conversão desejada: ")

        if escolha == "7":
            print("Saindo do programa. Até mais!")
            break

        try:
            temperatura = float(input("Digite a temperatura a ser convertida: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            continue

        if escolha == "1":
            print(f"\n{temperatura}°C é igual a {CparaF(temperatura)}°F")
        elif escolha == "2":
            print(f"\n{temperatura}°C é igual a {CparaK(temperatura)}K")
        elif escolha == "3":
            print(f"\n{temperatura}K é igual a {KparaC(temperatura)}°C")
        elif escolha == "4":
            print(f"\n{temperatura}K é igual a {KparaF(temperatura)}°F")
        elif escolha == "5":
            print(f"\n{temperatura}°F é igual a {FparaK(temperatura)}K")
        elif escolha == "6":
            print(f"\n{temperatura}°F é igual a {FparaC(temperatura)}°C")
        else:
            print("Escolha inválida, por favor tente novamente.")

main()
