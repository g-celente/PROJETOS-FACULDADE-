import random

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

def criar_matriz(lines, coluns):
    matriz = []
    for i in range(lines):
        i = []
        for j in range(coluns):
            linha = random.randint(0,200)
            i.append(linha)
        matriz.append(i)
    return matriz



def menu():
    
    while True:
        try:
            lines = int(input("Digite o números de linhas:\n> "))
            coluns = int(input("Digite o número de colunas:\n> "))
        except:
            print("Opção inválida, tente novamente...")
            continue

        matriz = criar_matriz(lines,coluns)
        imprimir_matriz(matriz)


if __name__=="__main__":
    menu()

