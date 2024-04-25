n = int(input("Digite o valor de N: "))
res = 0
for i in range(1, n+1):
    res += 1/i
print("O resultado é {}".format(res))