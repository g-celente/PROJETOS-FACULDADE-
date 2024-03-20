p = []
i = []
while True:    
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        p.append(numero)
    
    else:
        i.append(numero)
    print(f"Os números pares são: {p}")
    print(f"Os números impares são: {i}")
