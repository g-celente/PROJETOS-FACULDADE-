import sys
import time as t

conjA = []
conjB = []

sets=lambda a,b: (set(a),set(b))

def conjunts (ListaA, ListaB):
    while True:
        try:
            numA = int(input("Digite os valores do conjunto A e 0 para parar: "))
        except:
            print("Inválido, tente novamente...")
            continue

        if numA != 0: 
            ListaA.append(numA)
            
        else:
            print(f"O conjunto A é igual a: {ListaA}")
            print(80*'-')
            break
    
    while True:
        try:
            numB = int(input("Digite os valores do conjunto B e 0 para parar: "))
        except:
            print("Inválido, tente novamente...")
            continue
        
        if numB != 0:
            ListaB.append(numB)
            
        else:
            print(f"O conjunto B é igual a: {ListaB}")
            print(80*'-')
            break
            

def subconjunto(A,B):
    if A <= B:
        print("A é um subconjunto de B")
    
    else:
        print("A não é um subconjunto de B")
    t.sleep(2)

uniao = lambda A,B: A|B

intersencao= lambda A,B: A & B 

diferenca= lambda A,B: A-B


def set_intro ():
    global conjA, conjB
    conjunts(conjA, conjB)
    conjA, conjB = sets(conjA,conjB)

    while True:
        print(20*'-', "Conjuntos Numéricos", 20*"-")
        print("Escolha uma das opções: ")
        print(" 1 - Verificar se A é subconjunto próprio de B")
        print(" 2 - Realizar União dos Conjuntos")
        print(" 3 - Calcular intersenção ")
        print(" 4 - Calcular diferença")
        print(" 5 - Voltar ao menu principal")
        print(" 6 - Fechar calculadora")
        try:    
            choice = int(input("> "))
        except:
            print("Opção errada, tente novamente...")
            continue

        if choice == 1:
            subconjunto(conjA,conjB)
        elif choice == 2:
            print(f"A união dos conjuntos A e B é:\n> = {uniao(conjA,conjB)}")
            t.sleep(2)
        elif choice == 3:
            print(f"A intersenção dos conjuntos A e B é: \n> = {intersencao(conjA,conjB)}")
            t.sleep(2)
        elif choice == 4:
            print(f"A diferença dos conjuntos A e B é:\n> = {diferenca(conjA,conjB)}")
            t.sleep(2)       
        elif choice == 5:
            print("Voltando ao menu principal")
            break
        elif choice == 6:
            print("Obrigado por utilizar a calculadora")
            sys.exit()
        else:
            print("Opção inválida, tente novamente...")
            continue

