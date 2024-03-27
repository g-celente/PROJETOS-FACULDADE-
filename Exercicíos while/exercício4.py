b = int(input("Digite um número inteiro: "))
soma = 0 
contador = 1
while contador <= b:
    soma += contador
    contador += 1
print (f"A soma dos {b} primeiros números inteiros é: {soma}")