import conjuntos as cj
import exponecial as exp
import funcoes as fc
import matrizes as mt

while True:
    print(20*'-', "CALCULADORA", 20*'-')
    print("Escolha uma das Opções abaixo: ")
    print(" 1 - Conjuntos Numéricos")
    print(" 2 - Função do segundo Grau")
    print(" 3 - Função exponecial")
    print(" 4 - Matrizes")
    print(" 5 - Sair")

    while True:
        try:
            choice = int(input("> "))
        except:
            print("Operação inválida, tente um número inteiro")
            continue
        else:
            break

    if choice == 1:
        cj.set_intro()
    elif choice == 2:
        fc.def_intro()
    elif choice == 3:
        exp.exponential_intro()
    elif choice == 4:
        mt.mt_intro()
    elif choice == 5:
        choice2 = input("Deseja realmente sair? (s/n)\n> ").lower()
        if choice2 == "s":
            print("Obrigado por utilizar...")
            break
        elif choice2 == "n":
            continue
        else:
            print("Opção inválida")
            continue
    else:
        print("Opção inválida, tente novamente...")
        continue