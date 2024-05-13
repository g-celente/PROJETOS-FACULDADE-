import sys  

a = 0
b = 0


def verificar(A,B):
    pass

def calcular(A,B):
    pass

def grafico(A,B):
    pass

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
            verificar(a,b)
        elif choice == 2:
            calcular(a,b)
        elif choice == 3:
            grafico(a,b)
        elif choice == 4:
            print("Voltando ao menu principal")
            break
        elif choice == 5:
            print("Obrigado por utilizar a calculadora")
            sys.exit()
        else:
            print("Opção inválida, tente novamente...")
            continue