# 11. Elabore um programa que dado o peso de um boxeador, informe à categoria a qual 
# pertence, seguindo a tabela abaixo. 
# Categoria       Massa (Kg) 
# Palha           < 50 
# Pluma           < 59 
# Leve            < 75
# Pesado          < 87 
# Super Pesado    >= 87

peso = float(input("Digite o peso do boxeador: "))

categoria = ""

if(peso < 50):
    categoria = "Palha"
elif(peso < 59):
    categoria = "Pluma"
elif(peso < 75):
    categoria = "Leve"
elif(peso < 87):
    categoria = "Pesado"
elif(peso >= 87):
    categoria = "Super Pesado"
else:
    categoria = "Ops, algo deu errado..."

print("O atleta está classificado na categoria " + categoria)