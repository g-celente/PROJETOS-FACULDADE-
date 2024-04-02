#verdadeiro = True
#while verdadeiro: #isso se torna um loop infinito ou while true

#você deve aprimorar e melhorar usando o while true

#cont = 0 

#while True:
    #print (cont)
    #cont += 1 
    #if cont == 10: 
        #break #o break sai do loop e continua o código abaixo
#ja o continue, ele continua com o while, encerra e volta do ínicio 

#EXERCÍCIOS
#PROGRAMA PARA IDENTIFICAR NÚMEROS PARES E IMPARES

numeros_pares = 0
numeros_impares = 0
soma_pares = 0
soma_impares = 0

while True: 
    numero =  int(input("Digite um número positivo: "))
    if numero < 0:
        print("Numero inválido, digite um numero novamente...")
        continue
    #esse bloco acaba sendo independente, então o continue não da opção abaixo
    #crie um bloco independente usando outro if como bloco independente 

    #bloco independente para saber os pares
    if numero %2 == 0:
        print("Esse número é Par")
        numeros_pares += 1
        soma_pares += numero 
    else: 
        print("Esse número é impar")
        numeros_impares+=1 
        soma_impares += numero 

    if numeros_pares == 5 or soma_impares >= 30:
        break 
print(f"A quantidade de números pares fornecidos são: {numeros_pares}")
print(f"A quantidade de números impares fornecidos é igual a: {numeros_impares}")
print(f"A soma dos números pares é igual a: {soma_pares}")
print(f"A soma dos números impares é igual a: {soma_impares}")