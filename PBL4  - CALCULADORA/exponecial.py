import sys  
import matplotlib.pyplot as plt
import numpy as np

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
    return f_x
 

def grafico(A,B):
    x = float(input("Digite o valor de x: "))
    eixoX = np.arange(-10,11,1)
    eixoY = []

    for x in eixoX:
        fx = A * (B**x)
        eixoY.append(fx)
    plt.plot(eixoX,eixoY)
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.title("Gráfico de função 2° Grau")
    plt.grid(True)
    plt.axhline(y=0, color='r')
    plt.axvline(x=0, color='b')
    plt.show()
    
def exponential_intro ():
    a,b = 0, 0 
    while True:
        print(20*'-', "Funções Exponenciais", 20*"-")
        print("Escolha uma das opções: ")
        print(" 1 - Verificar se é crescente ou decrescente")
        print(" 2 - Calcular função em x pedido")
        print(" 3 - Gerar gráfico")
        print(" 4 - Pedir Valores")
        print(" 5 - Voltar ao menu principal")
        print(" 6 - Fechar calculadora")
        try:
            choice = int(input("> "))
        except:
            print("Opção inválida, tente novamente...")
            continue

        if choice == 1:
            verificar(a,b)
        elif choice == 2:
            calcular(a,b)
        elif choice == 3:
            grafico(a,b)
        elif choice == 4:
            a,b = numeros()
        elif choice == 5:
            print("Voltando ao menu principal")
            break
        elif choice == 6:
            print("Obrigado por utilizar a calculadora")
            sys.exit()
        else:
            print("Opção inválida, tente novamente...")
            continue