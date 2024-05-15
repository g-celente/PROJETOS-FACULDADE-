import sys  

a = 0
b = 0

def numeros ():
    done = False

    A = float(input("Digite o coeficiente de A:\n> "))
    
    while done == False:
        B = float(input("Digite o coeficiente de B:\n> "))

        if B <=0:
            print("O valor de B deve ser positivo!")
            continue
        done = True
    return A, B
    
def verificar(A,B):
    if B > 1:
        print("A função é crescente.")
    elif 0 < B < 1:
        print("A função é decrescente.")

def calcular(A,B):
    x = float(input("Digite o valor de x: "))
    
    f_x =  A * (B ** x)

    print(f"f({x}) = {f_x}")
    
 

def grafico(A,B):
    pass

def exponential_intro ():
    a, b = numeros()

    while True:
        print(20*'-', "Funções Exponenciais", 20*"-")
        print("Escolha uma das opções: ")
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