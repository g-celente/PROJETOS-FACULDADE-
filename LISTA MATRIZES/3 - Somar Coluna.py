def criar_matriz(lines, coluns):
    matriz = []
    for i in range(lines):
        i = []
        for j in range(coluns):
            linha = int(input("Digite um número:\n> "))
            i.append(linha)
        matriz.append(i)
    return matriz


def soma_coluna(matriz, coluna):

    if coluna < 0 or coluna >= len(matriz[0]):
        print("Coluna Inválida")

    soma = 0
    for linha in matriz:
        soma += linha[coluna]
    return soma

lines = int(input("Digite o números de linhas:\n> "))
coluns = int(input("Digite o número de colunas:\n> "))
matriz = criar_matriz(lines,coluns)

coluna = int(input("Digite qual coluna deseja realizar a operação:\n> "))
soma_col = soma_coluna(matriz, coluna)
print(f"Soma da coluna {coluna}:", soma_col)


