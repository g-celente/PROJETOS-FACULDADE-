def criar_matriz(lines, coluns):
    matriz = []
    for i in range(lines):
        i = []
        for j in range(coluns):
            linha = int(input("Digite um número:\n> "))
            i.append(linha)
        matriz.append(i)
    return matriz

def maior_valor_linha(matriz, linha):
    
    if linha < 0 or linha >= len(matriz):
        print("Matriz inválida...")
    else:
        return max(matriz[linha])

lines = int(input("Digite o números de linhas:\n> "))
coluns = int(input("Digite o número de colunas:\n> "))

matriz = criar_matriz(lines,coluns)

linha = int(input("Digite o número da linha:\n> "))
maior_valor = maior_valor_linha(matriz, linha)
print(f"Maior valor da linha {linha}:", maior_valor)