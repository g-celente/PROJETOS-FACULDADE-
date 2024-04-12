
numero = int(input("Digite um número para descobrir seus divisores: "))
divisores = []

for i in range(1,numero+1):
    if numero%i ==0:
        divisores.append(i)

print(f"Os divisores do {numero} são igual a: {divisores} ")