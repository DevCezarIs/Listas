# 19. Uma empresa deseja fazer o reajuste salarial dos seus funcionários da seguinte 
# forma: se o empregado for da categoria “Técnico”, receberá 30% de aumento, se for 
# da categoria “Gerente”, receberá 20% de aumento e os demais funcionários 
# receberão 15% de aumento. Faça um programa utilizando o comando if else aninhado 
# que leia do teclado o salário e a categoria do funcionário, calcule e imprima o seu 
# novo salário.  

print("===== Reajuste Salarial - Desperato Corp =====")

salario = float(input("Digite o seu salario: "))
categoria = int(input("Selecione sua categoria\nTécnico = 0\nGerente = 1\nOutro = 2\nDigite o código da sua categoria: "))

if(categoria == 0):
    salario *= 1.3
elif(categoria == 1):
    salario *= 1.2
elif(categoria == 2):
    salario *= 1.15
else:
    print("Erro: Categoria inválida.")
    exit()

print("Seu novo salário com o reajuste é de R${:.2f}".format(salario))