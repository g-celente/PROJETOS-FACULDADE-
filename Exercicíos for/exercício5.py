#LER 10 NÚMEROS INTEIROS E IMPRIMIR QUAL É PAR E QUAL É IMPAR

p = []
j = []

for i in range (0,10):
    while True:
        numero = int(input(f"Digite o {i + 1}° número: "))

        if numero < 0:
            print("Número inválido, tente novamente...")
            continue
        else:
            break

    if numero%2== 0:
        p.append(numero)

    else:
        j.append(numero)

print(f"Os números pares são:{p} ")
print(f"Os números impares são:{j} ")

