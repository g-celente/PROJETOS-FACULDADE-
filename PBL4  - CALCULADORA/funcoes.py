import sys

a = 0 
b = 0

def raiz (A,B):
    pass

def funcao (A,B):
    pass

def vertice(A,B):
    pass

def grafico(A,B):
    pass

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
            raiz(a,b)
        elif choice == 2:
            funcao(a,b)
        elif choice == 3:
            vertice(a,b)
        elif choice == 4:
            grafico(a,b)
        elif choice == 5:
            print("Voltando ao menu principal")
            break
        elif choice == 6:
            print("Obrigado por utilizar a calculadora")
            sys.exit()
        else:
            print("Opção inválida, tente novamente")
            continue