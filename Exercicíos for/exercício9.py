#LEIA 10 NÚMEROS E ARMAZE EM UMA LISTA COLOCANDO ELES EM ORDEM CRESCENTE
j = []

for i in range (0,10):
    numero = int(input(f"Digite o {i+1}° número: "))
    j.append(numero)
    
j.sort()
print(f"A ordem crescente dos números é: {j}")