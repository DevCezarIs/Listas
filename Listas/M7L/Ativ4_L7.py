"""
Escreva um programa que conta todas as vogais presentes no texto recebido como
parâmetro e retorna um dicionário contendo a quantidade de cada vogal. Seu
programa deve exibir, no fim, os dados do dicionário retornado.

"""
#Optei por funções por causa de sua versalidade....
def contador_vogais(texto):
    vogais = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    texto = texto.lower()
    for letra in texto:
        if letra in "aeiou":
            vogais[letra] += 1
    return vogais
def exibir_resultado(vogais):
    print("Contagem de vogais:")
    for vogal, quantidade in vogais.items():
        print(f"{vogal}: {quantidade}")

texto = input("Qual o texto será contado?\n")
resultado = contador_vogais(texto)
exibir_resultado(resultado)
