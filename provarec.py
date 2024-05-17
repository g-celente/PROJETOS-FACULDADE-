qtdIdade = 0
sum_idades = 0
cs2 = ['CS2',0,0]
dota2 = ['DOTA 2',0,0]
lol = ['League Of Legends',0,0]
valorant = ['Valorant',0,0]

def votos (lista,qtdIdade,sum_idades):
    while True:
        try:
            idade = int(input("Qual é a sua idade?\n: "))
            qtdIdade +=1 
            sum_idades += idade
        except:
            print("Opção inválida, tente novamente...")
            continue
        else:
            break
    media = sum_idades/qtdIdade

    lista[1] += 1
    lista[2] = media

def resultado (jogos):
    mais_votado = max(jogos, key=lambda x: x[1])

    for jogo in jogos:
        print(f'\n["{jogo[0]}", {jogo[1]}, {jogo[2]:.2f}]')

    print(f"O mais votado foi o {mais_votado[0]} {mais_votado[1]} pontos")
    print(f"A quantidade total de votos no mais votado foi {len(mais_votado)}")

while True:

    print("Escolha uma das opções abaixo: ")
    print("1 - CS2")
    print("2 - DOTA 2")
    print("3 - League Of Legends")
    print("4 - Valorant")
    print("5 - Resultado")
    print("6 - Sair")

    try:
        choice = int(input("> "))
    except:
        print("Opção inválida, tente novamente....")

    if choice == 1:
        votos(cs2,qtdIdade,sum_idades )
    elif choice == 2:
        votos(dota2,qtdIdade,sum_idades )
    elif choice == 3:
        votos(lol,qtdIdade,sum_idades )
    elif choice == 4:
        votos(valorant,qtdIdade,sum_idades )
    elif choice == 5:
        resultado([cs2, dota2, lol, valorant])
    elif choice == 6:
        print("Saindo...")
        break
    else:
        print("Jogo inexistente, tente novamente...")
        continue


        
