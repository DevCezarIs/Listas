# 23. Em um cinema que possui capacidade de 50 lugares foi distribuído um questionário 
# aos expectadores, no qual constava a idade e a sua opinião em relação ao filme, 
# segundo: ótimo, bom, regular, ruim ou péssimo. Elabore um programa que, lendo 
# estes dados, de diversos espectadores (até o limite de capacidade do cinema) calcule 
# e imprima: 
# a. A quantidade de respostas ótimo, bom, regular, ruim e péssimo. 
# b. A percentagem de ótimo, bom, regular, ruim e péssimo. 
# c. A idade do mais velho entrevistado. 
# d. A idade do mais novo entrevistado. 

print("<o> Coletor de Feedback iniciado <o>")

newer = 999
older = 0
stop = False

answers = 0

feedback0 = 0
feedback1 = 0
feedback2 = 0
feedback3 = 0
feedback4 = 0

while stop != True | answers < 50:
    print("|==========> Cadastrando Feedback (#{}) <==========|".format((answers + 1)))
    
    idade = int(input("Digite a idade do espectador: "))
    if idade < newer:
        newer = idade
    if idade > older:
        older = idade
    
    feedback = int(input("""
========================================
| Tabela de Feedback
| 0 = Péssimo
| 1 = Ruim
| 2 = Regular
| 3 = Bom
| 4 = Ótimo
| Digite o Feedback do espectador de acordo com a tabela acima: """))
    if feedback == 0:
        feedback0 += 1
    elif feedback == 1:
        feedback1 += 1
    elif feedback == 2:
        feedback2 += 1
    elif feedback == 3:
        feedback3 += 1
    elif feedback == 4:
        feedback4 += 1
    else:
        print("Ops, algo deu errado... Este feedback não foi cadastrado")
        continue
    
    answers += 1
    
    stopOrder = int(input("""
========================================
| Deseja fazer mais um cadastro?
| 
| Digite [0] para fazer mais um cadastro.
| Digite [1] ou qualquer outro número diferente de 0 para encerrar o programa e exibir os dados finais.
| 
| Digite o código do que deseja fazer: """))
    if stopOrder == 0:
        continue
    elif stopOrder == 1:
        break
    
print("""
      ============= Resultados finais =============
      | 
      | Quantidade de avaliações de cada grau:
      | > Péssimo: {}
      | > Ruim: {}
      | > Regular: {}
      | > Bom: {}
      | > Ótimo: {}
      | 
      | Quantidade percentual de avaliações em cada grau:
      | > Péssimo: {:.1f}%
      | > Ruim: {:.1f}%
      | > Regular: {:.1f}%
      | > Bom: {:.1f}%
      | > Ótimo: {:.1f}%
      | 
      | Maior idade de espectador: {}
      | Menor idade de espectador: {}
      |
      =============================================
      """.format(feedback0, feedback1, feedback2, feedback3, feedback4, feedback0*100/answers, feedback1*100/answers, feedback2*100/answers, feedback3*100/answers, feedback4*100/answers, older, newer))