"""
Faça um programa que leia nomes de alunos e suas respectivas notas até que o
nome ’oooo’ seja informado, após o fim da leitura, exiba o nome do aluno que possui
a maior nota. Obs.: Use dicionário para resolver essa questão.
"""

alunos = {}
nome_maior_nota = None
maior_nota = float('')

while True:
    nome = input("Digite o nome do aluno (ou 'oooo' para sair): ")
    if nome == 'oooo':
        break

    nota = float(input("Digite a nota do aluno: "))
    
    alunos[nome] = nota
    
    if nota > maior_nota:
        maior_nota = nota
        nome_maior_nota = nome

print(f"Alunos e suas notas: {alunos}")
print(f"Aluno com a maior nota: {nome_maior_nota} com nota {maior_nota}")

