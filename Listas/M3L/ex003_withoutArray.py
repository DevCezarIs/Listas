# 3. Escreva um programa que, dadas duas datas, determine qual delas ocorreu 
# cronologicamente primeiro. Para cada uma das duas datas, leia três números 
# referentes ao dia, mês e ano, respectivamente.

print("=====INICIO DO PROGRAMA=====")

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

maxDay1 = 0
maxDay2 = 0


# Verificação mês 1
if (mes1 == 2 and ano1 % 4 == 0):
    maxDay1 = 29
elif (mes1 == 2 and ano1 % 4 != 0):
    maxDay1 = 28
elif ((mes1 < 7 and mes1 % 2 == 0) or (mes1 >= 7 and mes1 % 2 != 0)):
    maxDay1 = 31
else: 
    maxDay1 = 30

# Verificação mês 2
if (mes2 == 2 and ano2 % 4 == 0):
    maxDay2 = 29
elif (mes2 == 2 and ano2 % 4 != 0):
    maxDay2 = 28
elif ((mes2 < 7 and mes2 % 2 == 0) or (mes2 >= 7 and mes2 % 2 != 0)):
    maxDay2 = 31
else: 
    maxDay2 = 30

if (mes1 > 12 or mes2 > 12):
    print("ERRO: Mês inválido")
    exit()

# Armazenando as datas no template padrão usado, mais fácil de ler (DD/MM/AAAA)
# datas = ["{}/{}/{}".format(dia1, mes1, ano1), "{}/{}/{}".format(dia2, mes2, ano2)]
data1 = str(dia1) + "/" + str(mes1) + "/" + str(ano1)
data2 = str(dia2) + "/" + str(mes2) + "/" + str(ano2)

# Variável que armazena o resultado da comparação, ela vai armazenar o index do dia que vem primeiro na comparação das duas datas
primeiro = 0

# Validação dos dados

if (ano1 % 4 == 0):
    # Ano bissexto
    if (dia1 > maxDay1 or dia1 < 0 and mes1 != 1):
        print("Aviso: Dia 1 invalido!")
    elif (dia1 > (maxDay1 + 1) or dia1 < 0 and mes1 == 1):
        print("Aviso: Dia 1 invalido!")
    elif (dia2 > maxDay2 or dia2 < 0 and mes2 != 1):
        print("Aviso: Dia 2 invalido!")
    elif (dia2 > (maxDay2 + 1) or dia2 < 0 and mes2 == 1):
        print("Aviso: Dia 2 invalido!")
else:
    # Ano não bissexto
    if (dia1 > (maxDay1) or dia1 < 0):
        print("Aviso: Dia 1 invalido!")
    elif (dia2 > maxDay2 or dia2 < 0):
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

if (primeiro == 0):
    print(data1 + " vem primeiro, " + data2 + " vem depois!") 
elif (primeiro == 1):
    print(data2 + " vem primeiro, " + data1 + " vem depois!") 
elif (primeiro == 2):
    print("Ambas as datas são iguais.")
else: 
    print("Algo deu errado :/")
    
print("=====FIM DO PROGRAMA=====")