import random 

pokemons_floresta = ["Treecko", "Torterra", "Venusaur", "Bayleef", "Ivysaur", "Sceptile","Flygon","Eevee","Garchomp","Greninja"]
pokemons_caverna = ["Meowscarada", "Chein-Pao", "Panda", "Gengar", "HeraCross", "Blaziken","Luxray","Tyranitar","Gardevoir","Lucario"]
pokedex = []
chances = 3

print("Olá, Seja bem vindo a Aventura Pokemón.",)
print("Eu sou o Professor Carvalho e estou aqui para lhe auxiliar nessa jornada Pokemon!")
nome_jogador = input("Antes de tudo, Qual é o seu nome? ")
print(" ")
print(f"Prazer {nome_jogador}!, Fico feliz que esteja aqui!...")
print("Nesta jornada, você poderá escolher 4 opções para realizar!.\n Caso escolha entrar na floresta ou caverna, você terá somente 3 chances de recaptura, então as use com sabedoria! Bom jogo")
print(" ")

while True:
    escolha = int(input("Oque deseja fazer?\n 1 - Entrar Floresta\n 2 - Entrar Caverna\n 3 - Ver Pokedex\n 4 - Sair\n Digite a Opção Desejada: "))
    
    if escolha == 1:
        capturas = random.randint(1,100)
        pokemon_encontrado = random.choice(pokemons_floresta)

        if pokemon_encontrado in pokedex:
                print(f"Você entrou na floresta encontrou o {pokemon_encontrado}, mas ele já está em sua pokedex, tente novamente")
                continue
         
        captura = input(f"Você entrou na floresta e encontrou o {pokemon_encontrado}, Deseja capturá-lo? (s/n) ").lower()

        if captura == "s":
            if capturas >= 50:
                print(f"Você capturou o {pokemon_encontrado}!")
                pokedex.append(pokemon_encontrado)
                continue
                
            else: 
                while True:
                    recaptura = random.randint(1,100)

                    if chances == 0:
                        print("Você não conseguiu Capturar! sem chances extras! Pokemon Escapou!")
                        break

                    recapturas = input(f"Você não conseguiu capturá-lo, deseja tentar novamente (s/n) (restam {chances} chances)? ").lower()

                    if recapturas == "s":
                        chances = chances - 1

                        if recaptura >=50:
                            print(f"Você capturou o {pokemon_encontrado}!")
                            pokedex.append(pokemon_encontrado)
                            break
                            
                        else:
                            continue

                    elif recapturas == "n":
                        print("Pokemon fugiu!!")
                        break
                    else:
                        print("Opção inválida, Pokemon escapou!")
                        break

        else:
            print("Pokemon escapou!")
            continue

    elif escolha == 2:
        capturas = random.randint(1,100)
        pokemon_encontrado = random.choice(pokemons_caverna)

        if pokemon_encontrado in pokedex:
                print(f"Você entrou na caverna encontrou o {pokemon_encontrado}, mas ele já está em sua pokedex, tente novamente")
                continue
         
        captura = input(f"Você entrou na caverna e encontrou o {pokemon_encontrado}, Deseja capturá-lo? (s/n) ").lower()

        if captura == "s":
            if capturas <= 35:
                print(f"Você capturou o {pokemon_encontrado}!")
                pokedex.append(pokemon_encontrado)
                continue
                
            else: 
                while True:
                    recaptura = random.randint(1,100)

                    if chances == 0:
                        print("Você não conseguiu Capturar! sem chances extras! Pokemon Escapou!")
                        break

                    recapturas = input(f"Você não conseguiu capturá-lo, deseja tentar novamente (s/n) (restam {chances} chances)? ").lower()

                    if recapturas == "s":
                        chances = chances - 1

                        if recaptura <=35:
                            print(f"Você capturou o {pokemon_encontrado}!")
                            pokedex.append(pokemon_encontrado)
                            break
                
                        else:
                            continue

                    elif recapturas == "n":
                        print("Pokemon fugiu!!")
                        break
                    else:
                        print("Opção inválida, Pokemon escapou!")
                        break
        else:
            print("Pokemon escapou!")
            continue

    elif escolha == 3:
        print(f"Os Pokemons na sua pokedex são:")
        for x in pokedex:
            print(F" - {x}")
    
    elif escolha == 4:
        print("Obrigado por jogar!")
        break

    else:
        print("Opção inválida, tente novamente...")
        continue