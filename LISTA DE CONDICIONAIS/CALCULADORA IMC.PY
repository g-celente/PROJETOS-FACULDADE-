while True:
    print("Olá, Vamos descobrir seu peso ideal")
    altura = float(input("Digite Sua altura: "))
    print("Digite qual é seu sexo abaixo")
    print(" 1 - Masculino")
    print(" 2 - Feminino")
    sexo = str(input("Escolha seu sexo: "))
    if sexo == "1":
        peso_ideal = (72.7* altura) - 58
    elif sexo == "2":
        peso_ideal = (62.1*altura) - 44.7
    print (F"Seu peso ideal é igual a: {peso_ideal:.2f}")
    
