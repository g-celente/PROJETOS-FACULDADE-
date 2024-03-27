print("Descubra se o número é impar ou par!!")
i = 0 
impares= 0
pares = 0
while i <= 10:
    numero1 = int(input("Digite seu número aqui:\n"))
    i += 1 
    if numero1 % 2 == 0:
        pares += 1
    else:
        impares += 1
print (f"A quantidade de números pares são: {pares} ")
print (f"A quantidade de números impares são: {impares}")

    

    