# 3. Escreva um programa que, dadas duas datas, determine qual delas ocorreu 
# cronologicamente primeiro. Para cada uma das duas datas, leia três números 
# referentes ao dia, mês e ano, respectivamente.

print("=====INICIO DO PROGRAMA=====")

maxDay = [31, # Janeiro 0
        28, # Fevereiro 1
        31, # Março 2
        30, # Abril 3
        31, # Maio 4
        30, # Junho 5
        31, # Julho 6
        31, # Agosto 7
        30, # Setembro 8
        31, # Outubro 9
        30, # Novembro 10
        31 # Dezembro 11
        ]

        # Padrão: se é menor que 7, os dias ímpares tem 30 e pares tem 31, isso se inverte do 7 pra cima
        # Exceção: fevereiro

print("Seja bem vindo ao programa comparador de datas")

# Coleta de dados

dia1 = int(input("Digite o número primeiro dia: "))
mes1 = int(input("Digite o mês do primeiro dia: "))
ano1 = int(input("Digite o ano do primeiro dia: "))
dia2 = int(input("Digite o número segundo dia: "))
mes2 = int(input("Digite o mês do segundo dia: "))
ano2 = int(input("Digite o ano do segundo dia: "))

if (mes1 > 12 or mes2 > 12):
    print("ERRO: Mês inválido")
    exit()

# Armazenando as datas no template padrão usado, mais fácil de ler (DD/MM/AAAA)
datas = ["{}/{}/{}".format(dia1, mes1, ano1), "{}/{}/{}".format(dia2, mes2, ano2)]

# Variável que armazena o resultado da comparação, ela vai armazenar o index do dia que vem primeiro na comparação das duas datas
primeiro = 0

# Validação dos dados

if (ano1 % 4 == 0):
    # Ano bissexto
    if (dia1 > maxDay[mes1 - 1] or dia1 < 0 and mes1 != 1):
        print("Aviso: Dia 1 invalido!")
    elif (dia1 > (maxDay[mes1 - 1] + 1) or dia1 < 0 and mes1 == 1):
        print("Aviso: Dia 1 invalido!")
    elif (dia2 > maxDay[mes2 - 1] or dia2 < 0 and mes2 != 1):
        print("Aviso: Dia 2 invalido!")
    elif (dia2 > (maxDay[mes2 - 1] + 1) or dia2 < 0 and mes2 == 1):
        print("Aviso: Dia 2 invalido!")
else:
    # Ano não bissexto
    if (dia1 > (maxDay[mes1 - 1]) or dia1 < 0):
        print("Aviso: Dia 1 invalido!")
    elif (dia2 > maxDay[mes2 - 1] or dia2 < 0):
        print("Aviso: Dia 2 invalido!")
        
if (mes1 > 12 or mes1 < 0):
    print("Aviso: Mês 1 inválido!")
elif (mes2 > 12 or mes2 < 0):
    print("Aviso: Mês 2 inválido!")
    
if (ano1 < 0):
    print("Aviso: Ano 1 inválido!")
elif (ano2 < 0):
    print("Aviso: Ano 2 inválido!")
    
# Comparação das datas

if (ano1 > ano2):
    primeiro = 1
elif (ano2 > ano1):
    primeiro = 0
else:
    if (mes1 > mes2):
        primeiro = 1
    elif (mes2 > mes1):
        primeiro = 0
    else:
        if (dia1 > dia2):
            primeiro = 1
        elif (dia2 > dia1):
            primeiro = 0
        else:
            primeiro = 2

# Exibição do resultado

if (primeiro != 2):
    print("{} é a data que vem primeiro, {} vem depois!".format(datas[primeiro], datas[int(not primeiro)]))
elif (primeiro == 2):
    print("Ambas as datas são iguais.")
else: 
    print("Algo deu errado :/")
    
print("=====FIM DO PROGRAMA=====")