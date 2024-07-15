# 7. Defina uma matriz de caracteres para guardar um texto para fazer um editor de texto 
# que leia as várias linhas dadas pelo usuário e quando este digitar uma linha em 
# branco, reescreva o texto do usuário e imprima as seguintes estatísticas do texto: 
# número de caracteres digitados, número de espaços em branco e número de linhas. 

print("=== Editor de Texto ===")
savedText = ""
while True: 
    currentLine = input()
    if currentLine == "":
        break
    else:
        savedText += currentLine + "\n"

charCount = len(savedText.replace("\n", ""))
lineCount = list(savedText).count("\n")
blankCount = list(savedText).count(" ")
print("""
=== Estatísticas ===
> Texto:
{}

> Contagem de caracteres: {}
> Contagem de linhas: {}
> Contagem de espaços em branco: {}
      """.format(savedText, charCount, lineCount, blankCount))