def imprimeDadosPessoais():
    print('''
    Dados Pessoais: Cezar Isac
    Endereço: São José dos Campos
    Telefone: 12 90000-0000

''')

def imprimeDadosEmpresariais():
    print('''

    Empresa: Bona Petit
    Salário: R$ 2,100.00
    Contratação: 15/07/24

''')

def menu():
    opcao = -1
    while opcao < 1 or opcao > 3:
        print('''
    1. Imprimir dados pessoais
    2. Imprimir dados profisionais
    3. Sair
''')
        
        opcao = int(input("Digite sua opção: \n"))

        if opcao <1 or opcao >3:
            print("\t Você digitou um valor inválido \n")

        return opcao 

def main():
    escolha = menu()

    if escolha == 1:
        imprimeDadosPessoais()
    
    elif escolha == 2:
        imprimeDadosEmpresariais()
    
    else: 
        print("Saindo...")

if __name__ == "__main__":
    main()