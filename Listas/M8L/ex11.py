# 11. O seno de um ângulo em radianos, no intervalo de 0 à 2  pode ser calculado através 
# da série de McLaurin, apresentada a seguir:  + − + − = ! 7 ! 5 ! 3 ! 1 sen 7 5 3 x x x x x 
# a. Escreva uma função que converta um ângulo em graus para seu valor em 
# radianos ( rad 180  =  ) 
# b. Escreva uma função que receba como parâmetro um ângulo em graus, a precisão 
# requerida para o cálculo e retorne o seu seno, utilizando a função de conversão 
# graus-radiano feita anteriormente 
# c. Faça um programa que teste a sua função para cálculo do seno. 

# a
def graus_para_radianos(graus):
    pi = 3.141592653589793
    return graus * (pi / 180)


# b

def fatorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def seno_mc_laurin(angulo_graus, precisao):
    angulo_rad = graus_para_radianos(angulo_graus)
    seno = 0
    termo = angulo_rad
    n = 0
    
    while abs(termo) > precisao:
        termo = ((-1) ** n) * (angulo_rad ** (2 * n + 1)) / fatorial(2 * n + 1)
        seno += termo
        n += 1
    
    return seno

def main():
    angulo_graus = float(input("Digite o ângulo em graus: "))
    precisao = float(input("Digite a precisão requerida: "))
    
    seno_calculado = seno_mc_laurin(angulo_graus, precisao)
    
    print("Seno calculado para {} graus com precisão {}: {}".format(angulo_graus, precisao, seno_calculado))

main()
