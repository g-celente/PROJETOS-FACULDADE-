#LER UM VALOR INTEIRO DE 1 A 10 E IMPRIMIR A TABUADA
        
while True:
    numero = int(input("Digite um número inteiro: "))
    
    if numero < 1 or numero > 10:
        print("Número inválido, tente novamente")
        continue
    else:
        break

for i in range(0,11):
    print(f" {numero} x {i} = {numero*i}")