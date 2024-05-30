#CRIAR UM EXERCÍCIO DE QUE RETORNE UMA MATRIZ DE MXN 

#EXERCÍCIO 1
def matrizes(lines,coluns):
    matriz = []

    for i in range(lines):
        i = []
        for j in range(coluns):
            try:
                nm = int(input("Digite um valor: "))
            except:
                print("Tente novamente...")
            i.append(nm)
        matriz.append(i)
    return matriz
    

#EXERCÍCIO 2
def print_matriz(matriz):
    for line in matriz:
        print(line)

def main():
    while True:
        print(20*'-', 'Matrizes',20*'-')
        print("Selecione uma Opção: ")
        print(" 1 - Pedir Matrizes")
        print(" 2 - Sair")

        try:
            choice = int(input("> "))
        except:
            print("Tente novamente...")
            continue
        
        if choice == 1:
            while True:
                try:
                    lines = int(input("Digite o valor de linhas:\n> "))
                    coluns = int(input("Digite o valor de colunas:\n> "))
                    
                except:
                    print("Tente novamente...")
                    continue
                matriz = matrizes(lines, coluns)
                print_matriz(matriz)
                break
        elif choice == 2:
            break
        else:
            print("Opção inválida, tente novamente...")
            continue   

main()