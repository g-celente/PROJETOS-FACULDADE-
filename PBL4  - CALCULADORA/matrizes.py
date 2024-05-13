import sys
a = 0
b = 0

def matriz (A,B):
    pass

def multiplicacao (A,B):
    pass

def trasposta(A,B):
    pass

def mt_intro ():
    while True:
        print("Escola uma das opções: ")
        print(" 1 - Verificar se é matriz quadrada")
        print(" 2 - Multiplicação")
        print(" 3 - Matriz transposta ")
        print(" 4 -  Voltar ao menu principal")
        print(" 5 - Fechar calculadora")

        choice = int(input("> "))

        if choice == 1:
            matriz(a,b)
        elif choice == 2:
            multiplicacao(a,b)
        elif choice == 3:
            trasposta(a,b)
        elif choice == 4:
            print("Voltando ao menu principal")
            break
        elif choice == 5:
            print("Obrigado por utilizar a calculadora")
            sys.exit()
        else:
            print("Opção inválida, tente novamente")
            continue