import sys

conjA = {1,2,3,4,5,6,7}
conjB = {3,4,5,6}


def subconjunto(A,B):
    if A <= B:
        print("A é um subconjunto de B")
    
    else:
        print("A não é um subconjunto de B")


def uniao(A,B):
    pass

def intersencao(A,B):
    pass

def diferenca(A,B):
    pass

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
            subconjunto(conjA,conjB)
        elif choice == 2:
            uniao(conjA,conjB)
        elif choice == 3:
            intersencao(conjA,conjB)
        elif choice == 4:
            diferenca(conjA,conjB)
        elif choice == 5:
            print("Voltando ao menu principal")
            break
        elif choice == 6:
            print("Obrigado por utilizar a calculadora")
            sys.exit()
        else:
            print("Opção inválida, tente novamente...")
            continue