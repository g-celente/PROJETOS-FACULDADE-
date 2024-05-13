import sys

def set_intro ():
    while True:
        print("Escolha uma das opções: ")
        print(" 1 - Verificar se A é subconjunto próprio de B")
        print(" 2 - Realizar União dos Conjuntos")
        print(" 3 - Calcular intersenção ")
        print(" 4 - Calcular diferença")
        print(" 5 -  Voltar ao menu principal")
        print(" 6 - Fechar calculadora")

        choice = int(input("> "))

        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            print("Voltando ao menu principal")
            break
        elif choice == 6:
            print("Obrigado por utilizar a calculadora")
            sys.exit()
        else:
            print("Opção inválida, tente novamente...")
            continue

def def_intro (): 
    while True:
        print("Escola uma das opções: ")
        print(" 1 - Calcular raízes")
        print(" 2 - Calcular função em x pedido")
        print(" 3 - Calcular Vértice ")
        print(" 4 - Gerar gráfico")
        print(" 5 -  Voltar ao menu principal")
        print(" 6 - Fechar calculadora")

        choice = int(input("> "))

        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            print("Voltando ao menu principal")
            break
        elif choice == 6:
            print("Obrigado por utilizar a calculadora")
            sys.exit()
        else:
            print("Opção inválida, tente novamente...")
            continue

def exponential_intro ():
    while True:
        print("Escola uma das opções: ")
        print(" 1 - Verificar se é crescente ou decrescente")
        print(" 2 - Calcular função em x pedido")
        print(" 3 - Gerar gráfico")
        print(" 4 -  Voltar ao menu principal")
        print(" 5 - Fechar calculadora")

        choice = int(input("> "))

        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            print("Voltando ao menu principal")
            break
        elif choice == 5:
            print("Obrigado por utilizar a calculadora")
            sys.exit()
        else:
            print("Opção inválida, tente novamente...")
            continue

def matrices_intro ():
    while True:
        print("Escola uma das opções: ")
        print(" 1 - Verificar se é matriz quadrada")
        print(" 2 - Multiplicação")
        print(" 3 - Matriz transposta ")
        print(" 4 - Calcular diferença")
        print(" 5 -  Voltar ao menu principal")
        print(" 6 - Fechar calculadora")

        choice = int(input("> "))

        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            print("Voltando ao menu principal")
            break
        elif choice == 6:
            print("Obrigado por utilizar a calculadora")
            sys.exit()
        else:
            print("Opção inválida, tente novamente...")
            continue


while True:
    print(100*'-')
    print("CALCULADORA")
    print("Escolha uma das Opções abaixo: ")
    print(" 1 - Conjuntos Numéricos")
    print(" 2 - Função do segundo Grau")
    print(" 3 - Função exponecial")
    print(" 4 - Matrizes")
    print(" 5 - Sair")

    choice = int(input("> "))

    if choice == 1:
        set_intro()
    elif choice == 2:
        def_intro()
    elif choice == 3:
        exponential_intro()
    elif choice == 4:
        matrices_intro()
    elif choice == 5:
        choice2 = int(input("Deseja realmente sair? (s/n)")).lower()
        if choice2 == "s":
            print("Obrigado por utilizar...")
            break
        elif choice2 == "n":
            continue
        else:
            print("Opção inválida")
            continue
    else:
        print("Opção inválida, tente novamente...")
        continue