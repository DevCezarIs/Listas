# 3. Para fazer o balanço mensal de um armazém, faça um programa que que leia para um 
# número qualquer de mercadorias diferentes o preço de custo, o preço de venda e a 
# quantidade vendida. A partir desses dados imprima: o número total de mercadorias 
# diferentes lidas, o faturamento total e o lucro total do armazém.

mercadorias = []

programState = 1

contadorMercadorias = 0

print("|===| Balanço mensal do armazém Desperato Corp |===|")

while programState != 0:
    mercadoria = ["Nome", 0, 0, 0]
    mercadoria[0] = input("Digite o nome da mercadoria: ") # Nome
    mercadoria[1] = float(input("Digite o preço de custo de '{}': ".format(mercadoria[0]))) # Preço de custo
    mercadoria[2] = float(input("Digite o preço de venda de '{}': ".format(mercadoria[0]))) # Preço de venda
    mercadoria[3] = int(input("Digite o total de vendas de '{}': ".format(mercadoria[0]))) # Quantidade vendida
    mercadorias.append(mercadoria)
    contadorMercadorias += 1
    programState = int(input("O que você deseja fazer?\nDigite 0 para encerrar o programa e visualizar os dados\nDigite 1 para adicionar um novo tipo de mercadoria a análise\nCódigo da ação: "))

qtdTiposMercadorias = 0
qtdMercadorias = 0
faturamentoTotal = 0
lucroTotal = 0

for mercadoria in mercadorias:
    qtdTiposMercadorias += 1
    faturamentoTotal += mercadoria[2] * mercadoria[3]
    lucroTotal += (mercadoria[2] - mercadoria[1]) * mercadoria[3]
    qtdMercadorias += mercadoria[3]

print('''
|====== Resultado da análise ======
| 
| > Total de mercadorias: {}
| > Total de tipos de mercadorias: {}
| > Faturamento total: R${:.2f}
| > Lucro total: R${:.2f}
| 
|====== Desperato Corp ============
'''.format(qtdMercadorias, qtdTiposMercadorias, faturamentoTotal, lucroTotal))