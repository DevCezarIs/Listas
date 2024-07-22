def menu():
    opcao = -1
    while opcao < 1 or opcao > 3:
        print("=" *45)
        print(
            '''
            [1] 
            [2]
            [3] Sair
'''
        )
        print("=" *45)

        opcao = int(input("Digite a sua opção: \n"))

        if opcao < 1 or opcao > 3:
            print("Opção Inválida")
        else:
            return opcao
        
def main():
    opcao = menu()
    if opcao == 1:
        pass

main()
