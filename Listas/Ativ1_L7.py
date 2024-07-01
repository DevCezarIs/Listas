'''

Escreva um programa que recebe como entrada um número inteiro n. Em seguida,
seu programa deve receber as informações de n Pokémon (nome, tipo e ataque). Para
cada Pokémon seu programa deve armazenar as informações utilizando uma
estrutura de dicionário. No fim, seu programa deve imprimir o nome do Pokémon do
tipo “Fogo” com maior ataque. Você pode assumir que os valores de ataque são
inteiros positivos distintos e que pelo menos um Pokémon do tipo “Fogo” será
fornecido.
Exemplo de entrada:
4
Bulbasaur Planta 78
Charmander Fogo 83
Squirtle Água 87
Vulpix Fogo 72
Resposta:
Charmander

'''
def main():
    n = int(input("Quantos pokemons serão analisados? \n"))
    pokemons = []
    maior_poder = 0
    melhor_pokemon = None

    print(
          "Faça nesse formato:"
          "Nome Tipo Poder(apenas números)"
          )

    for _ in range(n):
        entrada_pokemon = input().split()
        nome = entrada_pokemon[0]
        tipo = entrada_pokemon[1]
        poder = int(entrada_pokemon[2])

        pokemon_cadastrado = {
            "nome": nome,
            "tipo": tipo,
            "poder": poder
        }

        pokemons.append(pokemon_cadastrado)
    
    for pokemon in pokemons:
        if pokemon["tipo"].lower() == "fogo":
            if pokemon["poder"] > maior_poder:
                melhor_pokemon = pokemon["nome"]
                maior_poder = pokemon["poder"]

    print(f"O pokemon com maior poder dessa lista foi o: {melhor_pokemon} com o poder de {maior_poder}!")
    print(f"Aqui está os pokemons cadastrados: \n {pokemons}")

main()
