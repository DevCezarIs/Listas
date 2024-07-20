"""
5. Implemente um programa com uma função que, dada uma lista, retorne outra lista,
com os elementos da lista original, sem repetições.
"""
def listOrganizer():
    print("Digite os elementos da lista. Pressione Enter sem digitar nada para finalizar.")
    lista = []
    elementos_adicionados = 0
    elementos_duplicados = 0
    
    while True:
        elemento = input("Adicione um elemento à lista: ")
        if elemento == "":
            break
        if elemento not in lista:
            lista.append(elemento)
            elementos_adicionados += 1
            print(f'Elemento "{elemento}" adicionado.')
        else:
            elementos_duplicados += 1
            print(f'O elemento "{elemento}" já está na lista e não será adicionado novamente.')
    
    return lista, elementos_adicionados, elementos_duplicados

def main():
    print("Bem-vindo ao programa de geração de listas sem repetições!")
    lista_sem_repeticoes, elementos_adicionados, elementos_duplicados = listOrganizer()
    
    print("\nLista final sem repetições:")
    print(lista_sem_repeticoes)
    print(f"\nTotal de elementos adicionados: {elementos_adicionados}")
    print(f"Total de elementos duplicados: {elementos_duplicados}")
    print(f"Total de elementos na nova lista: {len(lista_sem_repeticoes)}")
    print("\nObrigado por usar o programa!")

main()
