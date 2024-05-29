import sys
import time as t

def matrizes ():
    while True:
        try:
            lines = int(input("Digite o número de linhas da matriz:\n> "))
            coluns = int(input("Digite o número de colunas:\n> "))
        except:
            print("Opção inválida, tente novamente...")
            continue
        break
    return lines, coluns

def ask_matriz(lines, coluns):
    matriz = []

    for i in range(lines):
        i = []
        while True:
            for j in range(coluns):
                try:
                    num = int(input("Digite o valor:\n> "))
                except:
                    print("Opção inválida, tente novamente...")
                    continue
                i.append(num)
            break
        matriz.append(i)

    return matriz

matrix = lambda matrix: all(len(row) == len(matrix) for row in matrix)
    
def multiplicacao (matriz):
    while True:
        lines,coluns = matrizes()
        matriz2 = ask_matriz(lines,coluns)

        if len(matriz[0]) != len(matriz2):
            print("O número de linhas da primera matriz deve ser igual ao número de colunas da segunda")
            continue

        num_lines = len(matriz)
        num_cols = len(matriz2[0])
        result = []
        for i in range(num_lines):
            result.append([0] * num_cols)   
            
        for i in range(num_lines):
            for j in range(num_cols):
                for k in range(len(matriz2)):
                    result[i][j] += matriz[i][k] * matriz2[k][j]

        for lines in result:
            print(lines)
        break

def trasposta(matriz):
    num_lines = len(matriz)
    num_cols = len(matriz[0])
    result = []

    for i in range(num_cols):
        result.append([0] * num_lines)

    for i in range(num_lines):
        for j in range(num_cols):
            result[j][i] = matriz[i][j]
    return result

def print_matriz(matriz):
    for line in matriz:
        print(line)

def mt_intro ():
    lines, coluns = matrizes()
    matriz = ask_matriz(lines,coluns)

    while True:
        print(20*'-', "Matrizes", 20*"-")
        print("Escolha uma das opções: ")
        print(" 1 - Verificar se é matriz quadrada")
        print(" 2 - Multiplicação")
        print(" 3 - Matriz transposta ")
        print(" 4 - Voltar ao menu principal")
        print(" 5 - Fechar calculadora")

        try:
            choice = int(input("> "))
        except:
            print("Opção inválida, tente novamente...")
            continue
        if choice == 1:
            if matrix(matriz) == True:
                print("A matriz é quadrada")
            else:
                print("A matriz não é quadrada")
        elif choice == 2:
            multiplicacao(matriz)
        elif choice == 3:
            result = trasposta(matriz)
            print("Matriz Original:")
            print_matriz(matriz)
            print("Transposta:")
            print_matriz(result)
        elif choice == 4:
            print("Voltando ao menu principal")
            break
        elif choice == 5:
            print("Obrigado por utilizar a calculadora")
            sys.exit()
        else:
            print("Opção inválida, tente novamente")
            continue

