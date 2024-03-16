while True:
    numero1 = int(input("Digite o Primeiro Número: "))
    operacao = input("Digite a Operação (+, -, x, /) ou 's' para sair: ")

    # Verificando se o usuário deseja sair
    if operacao.lower() == 's':
        print("Encerrando a calculadora.")
        break

    numero2 = int(input("Digite o Segundo Número: "))

    if operacao == "+":
        resultado = numero1 + numero2
        print(f"A operação foi soma: {numero1} + {numero2} = {resultado}")
    elif operacao == "-":
        resultado = numero1 - numero2 
        print(f"A operação foi subtração: {numero1} - {numero2} = {resultado}")
    elif operacao.lower() == "x":
        resultado = numero1 * numero2
        print(f"A operação foi multiplicação: {numero1} * {numero2} = {resultado}")
    elif operacao == "/":
        # Verificando divisão por zero
        if numero2 == 0:
            print("Erro: divisão por zero.")
        else:
            resultado = numero1 / numero2
            print(f"A operação foi divisão: {numero1} / {numero2} = {resultado}")
    else:
        print("Operação inválida. Por favor, insira uma das seguintes operações: '+', '-', 'x', '/' ou 's' para sair.")