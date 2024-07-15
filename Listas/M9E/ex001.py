def main():
    lines = int(input("Enter the number of lines: "))
    columns = int(input("Enter the number of columns: "))

    matriz = [ ]
    for i in range(lines):
        line = []
        for j in range(columns):
            line.append(int(input()))
        matriz.append(line)
    print(matriz)

main()