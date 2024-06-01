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

def print_matriz(matriz):
    for line in matriz:
        print(line)

def sum_par(matriz):

    sum_par = 0

    for i in matriz:
        for j in i:
            if j%2 == 0:
                sum_par += j  
            
    print(f"A soma dos números pares da matriz é: {sum_par}")

def main():
    while True:
        print(20*'-', 'Matrizes',20*'-')
        print("Selecione uma Opção: ")
        print(" 1 - Pedir Matrizes")
        print(" 2 - Soma Matrizes")
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
            sum_par(matriz)
        elif choice == 3:
            break
        else:
            print("Opção inválida, tente novamente...")
            continue   

main()