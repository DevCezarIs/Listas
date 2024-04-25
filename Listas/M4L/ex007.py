# 7. Uma indústria de alimentos congelados tem capacidade para estocar até 5 toneladas 
# de produto pronto para venda. Faça um programa que controle o estoque dessa 
# empresa, lendo do teclado a produção em kg de cada dia (sendo que uma produção 
# igual a zero é utilizada para encerrar a leitura).

estoque = 0
capacidadeMax = 5000

print("=====> Controle de Estoque <=====")
diario = float(input("Digite a produção diária em kg: "))

estoque += diario

print('''
|== Controle de Estoque =====
|
| > Estoque atual: {}kg
| > Capacidade máxima: {}kg
|
|============================
'''.format(estoque, capacidadeMax))

while diario != 0:
    print("Dica: Digite 0 como produção diária para encerrar o programa!\n")
    diario = float(input("Digite a produção diária em kg: "))
    estoque += diario
    print('''
|== Controle de Estoque =====
|
| > Estoque atual: {}kg
| > Capacidade máxima: {}kg
|
|============================
    '''.format(estoque, capacidadeMax))
    if estoque >= capacidadeMax:
        print("Alerta: Capacidade máxima do estoque excedida!\n")

print("=====> Programa Encerrado <=====")