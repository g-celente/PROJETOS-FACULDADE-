import random 
import time as t

pokemons_floresta = ["Treecko", "Torterra", "Venusaur", "Bayleef", "Ivysaur", "Sceptile","Flygon","Eevee","Garchomp","Greninja"]
pokemons_caverna = ["Meowscarada", "Chein-Pao", "Panda", "Gengar", "HeraCross", "Blaziken","Luxray","Tyranitar","Gardevoir","Lucario"]
pokedex = []
chances = 3

def captura (ListaPokemons):
    nm = random.randint(0,100)

    if ListaPokemons == pokemons_floresta:

        if nm >= 50:
            validacao = 1
        else:
            validacao =  2
    else:
        if nm <=35:
            validacao = 1
        else:
            validacao = 2

    return validacao

def introdução ():
    name =  input("Digite Seu nome:\n").capitalize()
    print(100*'-')
    print(f"Olá {name}, Meu nome é professor Carvalho e estou aqui para te ajudar nessa jornada Pokemon!")
    print("Nessa jornada, você terá 2 opções de entrada, sendo floresta e caverna...")
    print("Para cada caminho, você terá uma chance de encontrar 0, 1 ou 2 pokebolas a mais!")
    print(100*'-')

def pokemon_inicial(pokedex):
    print("Antes de começar, escolha um pokemon inicial!")

    while True:
        print(" 1 - Squirtle ")
        print(" 2 - Charmander")
        print(" 3 - Bulbasaur ")
        
        choice = int(input("> "))

        if choice == 1:
            pokedex.append("Squirtle")
            print("Parabéns, seu pokemon inicial é o: Squirtle!")
            break
        elif choice == 2:
            pokedex.append("Charmander")
            print("Parabéns, seu pokemon inicial é o: Charmander!")
            break
        elif choice == 3:
            pokedex.append("Bulbasaur")
            print("Parabéns, seu pokemon inicial é o: Bulbasaur!")
            break
        else:
            print("Opção inválida, tente novamente...")
            continue
    t.sleep(2)
    
def pegar_pokemon(listaPokemons, pokedex):
    global chances
   
    pokemon_encontrado = random.choice(listaPokemons)

    if pokemon_encontrado in pokedex:
        print(f"Você entrou na floresta e encontrou {pokemon_encontrado} e já tem em sua pokedex, saindo")
        
    else:
        pokebola_extra = random.randint(0,2)
            
        if pokebola_extra == 0:
            print(f"Que pena, você não conseguiu nenhuma pokebola extra! ")
        else:
            print(f"Parabéns, você conseguiu {pokebola_extra} pokebolas extras")
            chances += pokebola_extra

        captura2 = input(f"Você encontrou o {pokemon_encontrado},deseja capturá-lo? (s/n) \n: ").lower()
                
        if captura2 == "s":
                
            if captura(listaPokemons) == 1:
                print(f"Você capturou o {pokemon_encontrado}!")
                pokedex.append(pokemon_encontrado)
                    
            else:
                recaptura(listaPokemons,pokedex,pokemon_encontrado)     
    

def recaptura(listaPokemons, pokedex,pokemon_encontrado):
    global chances
    while True:

        if chances == 0:
            print("Suas chances extras acabaram!")
            break
        recaptura2 = input(f"Você não conseguiu capturá-lo. Deseja tentar novamente? (s/n) restam {chances} extras: ")

        if recaptura2 == "s":
            chances -= 1

            if captura(listaPokemons) == 1:
                print(f"Você capturou o {pokemon_encontrado}")
                pokedex.append(pokemon_encontrado)
                break
            else:
                continue

        elif recaptura2 == "n":
            break
        else:
            print("Opção inválida, pokemon escapou!")
            break
    
            

def ver_pokedex(pokedex):
    print(f"Os Pokemons na sua pokedex são:")
    for x in pokedex:
        print(F" - {x}")
        

introdução()
pokemon_inicial(pokedex)

while True:
    print(100*"-")
    print("Vamos começar!, escolha uma opção abaixo: ")
    print(" 1 - Entrar na Caverna")
    print(" 2 - Entrar na Floresta")
    print(" 3 - Ver sua Pokedex")
    print(" 4 - Sair do jogo")

    choice = int(input("> "))    
    if choice == 1:
        pegar_pokemon(pokemons_caverna,pokedex)
    elif choice == 2:
        pegar_pokemon(pokemons_floresta,pokedex)
    elif choice == 3:
        ver_pokedex(pokedex)
    elif choice == 4:
        print("Obrigado por jogar!")
        break
    else:
        print("Opção incorreta, tente novamente...")
        continue