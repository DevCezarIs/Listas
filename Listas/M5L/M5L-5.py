voos = [221, 291, 331, 442, 447, 727]
assentos_disponiveis = [345 for _ in range(len(voos))]
indice = -1
senha = "0000"

while True:
    print(("_"*50))
    print("\nHOME".center(50))
    print("[1] Voos Hoje           [2] Fazer Reserva")
    print("[3] Cancelar Reserva    [4] Sair do Programa ")

    print()
    print("="*50)
    opcao = int(input("Escolha uma opção: "))
    print("="*50)
    
    if opcao == 1:
        print(f"VOOS DISPONÍVEIS".center(50))
        print("_"*50)
        for i in range(len(voos)):
            print(f"Número do voo: {voos[i]} | Assentos disponíveis: {assentos_disponiveis[i]}".center(50))
    
    elif opcao == 2:
        print(f'VOOS:'.center(50))
        for i in range(len(voos)):
            print(f"Número do voo: {voos[i]} | Assemtos disponíveis: {assentos_disponiveis[i]}".center(50))
        
        voo_reserva = int(input("Em qual voo será feita a reserva? \n Escreva o número dele aqui: "))
        
        for i in range(len(voos)):

            if voo_reserva == voos[i]:
                print("Voo encontrado!")
                indice = i
        if indice != -1:
            if assentos_disponiveis[indice] > 0:
                confirm = input(f"Deseja reservar o assento do voo {voo_reserva}? [S/N]\n")
                if confirm.lower().strip() == "s":
                    assentos_disponiveis[indice] -= 1
                    print("Voo reservado com sucesso. Te espero lá!")
                
                else: 
                        print("OK, Reserva Cancelada")
            else:
                print("Desculpe, Mas todos os assentos estão reservados.")
        else:
            print("Ops, voo não encontrado. Tente novamente agora digitando o número de 3 digitos do Voo disponível na tabela acima.")
    
    elif opcao == 3:
        print("ÁREA DE CANCELAMENTO DE RESERVA".center(50))

        voo_reserva = int(input("Digite o número do voo que deseja cancelar a sua reserva: "))

        for i in range(len(voos)):
            if voo_reserva == voos[i]:
                indice = i 
                break
        
        if indice != -1:
            if assentos_disponiveis[indice] < 345:
                assentos_disponiveis[indice] += 1
                print("Reserva cancelada com sucesso!")
            else:
                print("Esse voo não tem reservas. \n Verifique se digitou o número do voo corretamente e tente novamente.")
        else:
            print('Voo não encontrado. \n Verifque se digitou o número correto do voo e tente novamente.')

    elif opcao == 4:
        validacao_senha = (input("Qual a senha de acesso ao programa?\n"))
        if senha == validacao_senha:    
            print("Encerrando Programa.")
            break
        else: 
            print("Senha Inválida")

    else:
        print("Opção inválida, Digite apenas o número da opção desejada.")   