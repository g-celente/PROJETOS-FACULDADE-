while True:
    print ("Olá, vamos descobrir se você está aprovado!!")
    nota =  float(input("Digite Sua Nota Aqui: "))
    if nota >= 7:
        print("Você está Aprovado!")
    elif nota >= 4 and nota <= 7:
        print("Você está em Recuperação!")
        diferenca = 7-nota   
        print (f"Você está em recuperação por {diferenca:.2f}")
    else:
        print ("Infelizmente Você está reprovado")
