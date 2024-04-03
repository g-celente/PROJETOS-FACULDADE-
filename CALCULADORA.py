while True:
    print("---  MENU CALCULADORA --- ")
    print(" 1 - SOMA \n 2 - SUBTRAÇÃO \n 3 - MULTIPLICAÇÃO \n 4 - DIVISÃO \n 5 - SAIR")
    operacao = int(input("Digite a Operação desejada: "))
   
    if operacao == '5':
        print("Encerrando a calculadora.")
        break
    
    numero1 = int(input("Digite o Primeiro Número: "))
    numero2 = int(input("Digite o Segundo Número: "))

    if operacao == 1:
        resultado = numero1 + numero2
        print(f"A operação foi soma: {numero1} + {numero2} = {resultado}")
    elif operacao == 2:
        resultado = numero1 - numero2 
        print(f"A operação foi subtração: {numero1} - {numero2} = {resultado}")
    elif operacao == 3:
        resultado = numero1 * numero2
        print(f"A operação foi multiplicação: {numero1} * {numero2} = {resultado}")
    elif operacao == 4:
       resultado = numero1 / numero2 
       print(f"A divisão {numero1} / {numero2} = {resultado:.2f}")
       
    else:
        print("Operação inválida. Por favor, insira uma das seguintes operações: '1', '2', '3', '4' ou '5' para sair.")

    print("Obrigado!")
    print(80*"-")
    print(80*"-")
