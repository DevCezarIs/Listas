# 7. Um microempresário tem por norma retirar mensalmente 40% do lucro de sua 
# empresa para os seus gastos pessoais se o lucro ultrapassar R$ 3.000,00 e retirar 
# apenas R$ 1.000,00 se o lucro for menor que isso. Faça um programa que leia do 
# teclado o faturamento mensal e o total das despesas para calcular o lucro (lucro = 
# faturamento - despesas) e imprima quanto o microempresário deve retirar neste mês. 
# Declare com constantes simbólicas o lucro mínimo, a retirada mínima e o limite da 
# retirada. 

faturamento = float(input("Digite o faturamento mensal: "))
despesas = float(input("Digite as despesas do mês: "))

lucro = faturamento - despesas

minLucro = 1000
minRetirada = 1000
maxRetirada = lucro * 0.4 # Valor máximo deve respeitar 40% do lucro

retirada = 0

if(lucro > 3000):
    retirada = lucro * maxRetirada
elif(lucro == minLucro):
    retirada = minRetirada
else:
    retirada = 0

print("Seu lucro foi de R${:.2f}, portanto, você deve retirar R${:.2f} para gastos pessoais.".format(lucro, retirada))