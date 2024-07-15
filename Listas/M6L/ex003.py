# 3. Um palíndromo é uma palavra ou frase que pode ser lida da mesma forma tanto da 
# esquerda para a direita como da direita para a esquerda (desconsiderando os 
# espaços em branco). Considere que a entrada não possui sinais de pontuação ou 
# acentos. Escreva um programa que, dada uma String, verifique se ela é um 
# palíndromo. 

from unidecode import unidecode # Usando biblioteca usada para remover todas as ocorrências de acentos.

print("=== Verificador de Palíndromo ===")
palindromeTest = input("Digite a frase que deseja verificar se é um palíndromo: ")
palindromeTest = unidecode(palindromeTest).split(" ")
palindromeTest = "".join(palindromeTest).replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").replace("\"", "").replace("\'", "").strip().lower()
reverseText = list(palindromeTest)
reverseText.reverse()
reverseText = "".join(reverseText)
if(reverseText == palindromeTest):
    print("O texto é um palíndromo")
else:
    print("O texto não é um palíndromo")