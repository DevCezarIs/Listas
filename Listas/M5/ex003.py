# 3. Faça um programa para calcular a média de um conjunto de 15 valores dados pelo 
# usuário e armazenados em um vetor. Ao final, imprima a média e todos os valores 
# digitados que ficaram abaixo da média. 

values = []
sumValues = 0
lowerThanAverage = []
i = 0

while i < 15:
    inputRunning = input("Digite o {}° valor: ".format(i + 1))
    if not inputRunning.isnumeric():
        continue
    values.append(int(inputRunning))
    sumValues += values[i]
    i += 1

for i in range(0, 15):
    if values[i] < (sumValues / 15):
        lowerThanAverage.append(str(values[i]))
        
print("""
    ----------
    Média dos valores: {}
    
    Valores abaixo da média [{}]: {}
    ----------
      """.format((sumValues / 15), len(lowerThanAverage), ", ".join(lowerThanAverage)))