print ("insira um número, caso queira finalizar, digite -1 ")
contador = 0
soma = 0
while soma != -1:
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1   
    if numero == -1:
        print (f"A média é igual a: {soma/contador:.2f} ")
        break 
    