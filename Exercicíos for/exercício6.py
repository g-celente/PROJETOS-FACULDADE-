
p = []
j = []

for i in range (0,10):
    numero = int(input(f"Digite o {i+1}° numero: "))

    if numero < 0: 
        print("Número inválido, tente novamente...")
        continue
    
    if numero >= 10 and numero <=20:
        p.append(numero)
    
    else: 
        j.append(numero)

print(f"A quantidade de números dentro do intervalo [10,20]: {len(p)}")
print(f"A quantidade de números fora do intervalo é: {len(j)}")
