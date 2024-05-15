import sys

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
    print(f"A função é:\nf({x}) = {fx}")


def vertice(A,B,C):
    xv = -B / (2*A)
    yv = A*xv**2 + B*xv + C

    if A>0:
        tipo = "mínimo"
    else:
        tipo = "máximo"

    print(f"O vértice da função é ({xv}, {yv}) e é um ponto de {tipo}")

def grafico(A,B,C):
    largura = 60
    altura = 20
    escala_x = 0.5
    escala_y = 1.0
    
    # Gerar pontos da função quadrática
    pontos = []
    for i in range(largura):
        x = (i - largura // 2) * escala_x
        y = A * x**2 + B * x + C
        pontos.append((x, y))

    # Encontrar valores máximos e mínimos para escalar o gráfico
    min_y = min(p[1] for p in pontos)
    max_y = max(p[1] for p in pontos)

    # Desenhar o gráfico
    for j in range(altura, -1, -1):
        linha = ""
        for i in range(largura):
            x, y = pontos[i]
            scaled_y = (y - min_y) / (max_y - min_y) * altura
            if abs(scaled_y - j) < 0.5:
                linha += "*"
            elif j == altura // 2:
                linha += "-"
            elif i == largura // 2:
                linha += "|"
            else:
                linha += " "
        print(linha)

def def_intro ():
    print("Antes de tudo, informe os valores de A, B e C: ")
    a,b,c = valores()

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
            raiz(a,b,c)
        elif choice == 2:
            funcao(a,b,c)
        elif choice == 3:
            vertice(a,b,c)
        elif choice == 4:
            grafico(a,b,c)
        elif choice == 5:
            print("Voltando ao menu principal")
            break
        elif choice == 6:
            print("Obrigado por utilizar a calculadora")
            sys.exit()
        else:
            print("Opção inválida, tente novamente")
            continue