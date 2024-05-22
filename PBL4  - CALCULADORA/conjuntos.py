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

def uniao(A,B):
    uniao = A|B

    print(f"A união dos conjuntos A e B é {uniao}")
    t.sleep(2)
    
def intersencao(A,B):
    intersencao = A & B

    print(f"A interseção dos Conjuntos A e B é: {intersencao}")
    t.sleep(2)

def diferenca(A,B):
    diferenca = A-B
    
    print(f"A diferença dos Conjuntos A e B é: {diferenca}")
    t.sleep(2)

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

        choice = int(input("> "))

        if choice == 1:
            subconjunto(conjA,conjB)
        elif choice == 2:
            uniao(conjA,conjB)
        elif choice == 3:
            intersencao(conjA,conjB)
        elif choice == 4:
            diferenca(conjA,conjB)
        elif choice == 5:
            print("Voltando ao menu principal")
            break
        elif choice == 6:
            print("Obrigado por utilizar a calculadora")
            sys.exit()
        else:
            print("Opção inválida, tente novamente...")
            continue