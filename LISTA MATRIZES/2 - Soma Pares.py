
def criar_matriz(lines, coluns):
    matriz = []
    for i in range(lines):
        i = []
        for j in range(coluns):
            linha = int(input("Digite um número:\n> "))
            i.append(linha)
        matriz.append(i)
    return matriz

def sum_matriz (matriz):
    pares = []
    for i in matriz:
        for j in i:
            if j%2==0:
                pares.append(j)
    
    print(f"A soma dos números pares da matríz é {sum(pares)}")

lines = int(input("Digite o números de linhas:\n> "))
coluns = int(input("Digite o número de colunas:\n> "))

matriz = criar_matriz(lines,coluns)
sum_matriz(matriz)

    

