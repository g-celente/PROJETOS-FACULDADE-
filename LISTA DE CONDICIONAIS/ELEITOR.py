idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Eleitor!")
elif idade >= 16 and idade < 18:
    print ("Eleitor Facultativo!")
else:
    print ("Não Eleitor")