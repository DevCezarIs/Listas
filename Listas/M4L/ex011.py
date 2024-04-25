# 11. O volume de uma esfera pode ser calculado pela fórmula 3
#  3
#  4 r V  = , onde r é o raio da 
# esfera. Faça um programa que imprima uma tabela de volumes para esferas que 
# tenham raios entre 0 e 15 cm, de 0.5 em 0.5cm.

pi = 3.141592

for r in range(0, 155, 5):
    print("Raio: {}cm | Volume: {:.2f}cm³".format((r / 10), ((4*pi)/3) * (r/10)**3))