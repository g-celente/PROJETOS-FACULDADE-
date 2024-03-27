p = 0
i = 0
soma_impares = 0
soma_pares = 0
while p <= 5 and soma_impares <30:
    g = int(input("Digite um número: "))
    if g % 2 == 0:
        p += 1
        print("Esse número é par")
        soma_pares += g 
    elif g < 0:
        print("Número inválido, digite um número novamente")
    else:
        soma_impares += g 
        i += 1 
        print("Esse número é impar!")
print (f"A quantidade de números pares foram: {p} ")
print (f"A soma dos ímpares é igual a: {soma_impares}")
print (f"A soma dos pares são igual a : {soma_pares}")
print(f"A quantidade de números impares é: {i}")
