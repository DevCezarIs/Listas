# 27. O custo de produção de um livro é constituído dos custos por página, mais o custo 
# de encadernação, além do custo fixo. O custo por página impressa é de R$0,03, o 
# custo fixo é de R$ 4397,00 e o custo de encadernação depende de cada livro, sendo 
# utilizada a seguinte tabela:  
# • Encadernação simples: R$4,30 
# • Encadernação especial: R$7,80 
# • Encadernação luxo: R$10,50 
# Faça um programa que leia para uma lista de livros: o número de páginas, o tipo de 
# encadernação e o número de vendas previstas (número de cópias) e: 
# a. Calcule o preço mínimo de cada livro para que cubra os custos de produção e 
# o preço de venda para que a editora tenha um lucro de 20%.  
# b. Imprima o total de livros analisados. 
# c. Imprima o preço médio de venda dos livros (com lucro de 20%). 
# d. Imprima o preço de venda dos livros mais barato e mais caro.  

# calculo do preço
# p(0.03) + enc + fix(4397)

# cadastrar uma lista de livros

# arrayLivro = [pag, enc, selling]

livros = []
precoLivros = []

mostExpensive = 0
cheaper = 99999999999999

bookStringPrices = ""

encadernacaoPrecos = [4.3, 7.8, 10.5]

while True:
    print("=== Cadastro de Livro ===")
    pag = int(input("Digite o números de páginas do livro: "))
    enc = int(input("""
    === Encadernação ===
    | - Encadernação simples (R$4,30): Digite 0
    | - Encadernação especial (R$7,80): Digite 1
    | - Encadernação luxo (R$10,50): Digite 2
    Digite o código da encadernação: """))
    sell = int(input("Digite a quantidade de cópias: "))
    if enc <= 2 and enc >= 0:
        livros.append([pag, enc, sell])
    endLoop = int(input("Deseja continuar adicionando livros na análise? Digite [0] para não e [1] para sim: "))
    if endLoop != 0:
        continue
    else:
        break
    
for i in range(0, len(livros)):
    livro = livros[i]
    precoLivros.append((livro[0]*0.03 + encadernacaoPrecos[livro[1]] + 4397))
    if precoLivros[i]/livro[2] > mostExpensive:
        mostExpensive = precoLivros[i]/livro[2]
    if precoLivros[i]/livro[2] < cheaper:
        cheaper = precoLivros[i]/livro[2]
    bookStringPrices = bookStringPrices + str("\n| > Livro #{}\n| Preço mínimo de produção: R${:.2f}\n| Preço médio da unidade: R${:.2f}".format(i, (precoLivros[i]*1.2), (precoLivros[i]*1.2)/livro[2]))
        
        
print(str(livros))
print(str(precoLivros)) 
print("""
=== Resultados das análises dos livros ===
|
| Livros analisados: {}
|{}
|
| > Preço do livro mais caro: R${:.2f}
| > Preço do livro mais barato: R${:.2f}
|
==========================================
      """.format(len(livros), bookStringPrices, mostExpensive, cheaper))