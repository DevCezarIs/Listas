# 19. Faça um programa didático para estudo de tabuadas de 1 até 10, onde: 
# a. A criança escolhe a tabuada a ser estudada. 
# b. O programa gera um número aleatório e pergunta à criança qual o valor dele 
# multiplicado pela tabuada escolhida. Se a criança errar, o programa pergunta 
# novamente, se acertar o programa pergunta à criança se ela deseja continuar 
# respondendo. 
# c. Ao final, o programa deve imprimir o número de perguntas respondidas, o 
# número de acertos e o número de erros cometidos pela criança. 

from random import randint
import os

print("===== Treino de Tabuada =====")

# Loop do programa inteiro
while True:
    
    continueChallenge = False
    
    choice = int(input("""
    O que você quer fazer?
    • Ver tabuadas [1]
    • Resolver desafios [2]
    Digite o código do conteúdo que deseja acessar: """))
    
    if choice == 1:
        continueChallenge = False
        choiceTable = int(input("Digite o número que você deseja ver a tabuada: "))
        maxTable = 10
        if choiceTable > maxTable:
            maxTable = choiceTable
        if choiceTable >= 0:
            print("Tabuada do {}".format(choiceTable))
            for i in range(1, choiceTable + 1):
                print("{} x {} = {}".format(choiceTable, i, (choiceTable * i)))
        else:
            print("Ops, por favor, escolha um número inteiro positivo.")
    elif choice == 2:
        continueChallenge = True
    else:
        print("Ops, não entendi o que você quis dizer...")
        continue
    
    resolvidos = 0
    erros = 0
    negative = False
    # Loop dos desafios
    while continueChallenge == True:
        # Redefinindo os desafios
        
        num = int(input("""
    > Veja as tabuadas disponíveis: 
    • 1
    • 2
    • 3
    • 4
    • 5
    • 6
    • 7
    • 8
    • 9
    • 10
    Digite a tabuada desejada: """))
        
        max = 10
        if(num > 10 or num < 0):
            print(" > Hmmm, okay, parece que você quer um desafio...")
            max = num
            negative = True
        
        challenge = 0
        
        # Definindo o desafio, considerando se ela quer algo mais difícil ou não
        if negative:
            challenge = randint((max * -1), max)
        else:
            challenge = randint(0, max)
            
        # Loop do desafio (individual)
        while True:
            answerChallenge = int(input("Digite a resposta do seguinte desafio (digite [0] para desistir):\n{} * {}\nRespota: ".format(num, challenge)))
            if (num * challenge) == answerChallenge:
                print("Parabéns! Resposta correta!")
                resolvidos += 1
                break
            elif answerChallenge == 0:
                print("Ok, sem problemas...")
                break
            else:
                print("Ops, resposta errada, tente novamente")
                erros += 1
                continue
        
        # Verifica se ela quer continuar respondendo perguntas e, caso não queira
        answerContinue = int(input("Você deseja continuar respondendo desafios? [1] para sim e [0] para não: "))
        if answerContinue == 1:
            continue
        else:
            print("""
    | Certo, aqui estão seus resultados:
    |
    | > Acertos: {}
    | > Erros: {}
    | > Taxa de erros: {:.1f}%
                  """.format(resolvidos, erros, (erros * 100 / (erros + resolvidos))))
            break
    
    
    
    wannaExit = int(input("Deseja fechar o programa? \nDigite [1] para não e [0] para sim: "))
    if(wannaExit == 0):
        break
    os.system("cls")