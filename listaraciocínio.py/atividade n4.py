cont = 0
soma = 0
x =  int(input("Informe quantos números deseja somar: "))
while cont < x:
    numero = int(input(f"Digite o {cont+1}°: ")) 
    if numero <= 9: 
        print ("Número inválido, digite um maior que 10! ")
    else:
        cont += 1
    soma += numero
print (f"A soma dos números fornecidos é igual a: {soma}")
