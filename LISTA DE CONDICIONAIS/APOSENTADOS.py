print("Descubra se você pode se aposentar!")
idade = int(input("Digite sua Idade: "))
tempo_de_servico = int(input("Digite Seu Tempo de Serviço: "))
if idade >= 65:
    print ("Pode Se aposentar!")
elif tempo_de_servico >= 30:
    print ("Pode Se Aposentar!")
elif idade >= 60 and tempo_de_servico >= 25:
    print ("Pode se aposentar!")
else:
    print ("Não pode se aposentar")
    diferenca = 60 - idade 
    diferenca2 = 30 - tempo_de_servico
    print (f"Falta {diferenca:.2f} ano para se aposentar")
    print (f"Falta {diferenca2:.2f} anos de serviço para se aposentar")