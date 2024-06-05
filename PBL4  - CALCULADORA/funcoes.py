import sys
import numpy as np
import matplotlib.pyplot as plt

def valores ():
    done = False
    while not done:

        a = float(input("Digite o Valor de A:\n> "))

        if a == 0:
            print("O coeficiente a não pode ser igual a 0, tente novamente...")
            continue

        b = float(input("Digite o Valor de B:\n> "))
        c = float(input("Digite o Valor de C:\n> "))
        done = True    

    return a,b,c
def raiz (A,B, C):

    if A == 0 and B == 0 and C == 0:
        print("Por favor, primeiro insira os valores na opção 5")
    
    delta = B**2 - 4*A*C

    if delta > 0:
        raiz1 = (-B + delta**0.5)/(2*A)
        raiz2 = (-B - delta**0.5)/(2*A)

        print(f"As Raízes são Reais e diferentes:\nRaiz 1 = {raiz1}\nRaiz 2 = {raiz2}")

    elif delta == 0:
        raiz1 = -B/(2*A)
        raiz2 = raiz1
        print(f"As Raízes são iguais:\nRaiz 1 = {raiz1}\nRaiz 2 = {raiz2}")

    else:
        real = -B / (2*A)
        imaginario = (-delta)**0.5 / (2*A)
        raiz1 = complex(real, imaginario)
        raiz2 = complex(real, -imaginario)

        print(f"As Raízes são complexas:\nRaiz 1 = {raiz1}\nRaiz 2 = {raiz2}")

def funcao (A,B,C):
    x = float(input("Digite o valor de x:\n> "))
    fx = A*x**2 + B*x + C
    print(f"A função gerada é:\nf({x}) = {fx}")
    


def vertice(A,B,C):
    xv = -B / (2*A)
    yv = A*xv**2 + B*xv + C

    if A>0:
        tipo = "mínimo"
    else:
        tipo = "máximo"

    print(f"O vértice da função é ({xv}, {yv}) e é um ponto de {tipo}")

def grafico(A,B,C):
    x = float(input("Digite o valor de x:\n> "))
    eixoX = np.arange(-10,11,1)
    eixoY = []

    for x in eixoX:
        fx = A*x**2 + B*x + C
        eixoY.append(fx)
    
    plt.plot(eixoX,eixoY)
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.title("Gráfico de função 2° Grau")
    plt.grid(True)
    plt.axhline(y=0, color='r')
    plt.axvline(x=0, color='b')
    plt.show()
    
def def_intro ():
    
    while True:
        print(20*'-', "Funções Segundo Grau", 20*"-")
        print("Escolha uma das opções: ")
        print(" 1 - Calcular raízes")
        print(" 2 - Calcular função em x pedido")
        print(" 3 - Calcular Vértice ")
        print(" 4 - Gerar gráfico")
        print(" 5 - Pedir Valores")
        print(" 6 - Voltar ao menu principal")
        print(" 7 - Fechar calculadora")
        try:
            choice = int(input("> "))
        except:
            print("Opção inválida, tente novamente...")
            continue
        
        try:
            if choice == 1:
                raiz(a,b,c)
            elif choice == 2:
                funcao(a,b,c)
            elif choice == 3:
                vertice(a,b,c)
            elif choice == 4:
                grafico(a,b,c)
            elif choice == 5:
                a,b,c = valores()
            elif choice == 6:
                print("Voltando ao menu principal")
                break
            elif choice == 7:
                print("Obrigado por utilizar a calculadora")
                sys.exit()
            else:
                print("Opção inválida, tente novamente")
                continue
        except:
            print("Por favor, primeiro insira os valores na opção 5")