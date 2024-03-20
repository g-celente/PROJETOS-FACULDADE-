print ("Escolha Sua Faculdade")
print (" 1 - PUC")
print (" 2 - UNICAMP")
faculdade = int(input("Digite Sua Faculdade: "))
media =  float(input("Digite Sua Media: "))

if faculdade == 1 and media >= 7:
    print ("Você está aprovado!")
elif faculdade == 1 and media >= 4 and media < 7:
    print ("Você está em recuperação")
elif faculdade == 1 and media < 4:
    print ("Você está reprovado!")
elif faculdade == 2 and media >= 5:
    print ("Aprovado")
elif faculdade == 2 and media < 5: 
    print ("Em Exame")