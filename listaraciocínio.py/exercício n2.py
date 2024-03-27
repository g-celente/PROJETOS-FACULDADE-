soma = 0 
contador = 0
while contador <= 10:
    nota = float(input("Digite uma nota: "))
    if nota >10 or nota <0:
        print ("Nota inválida, digite novamente...")
    else: 
        soma += nota
        contador += 1
media_notas = soma / contador  
print(f"A media das somas é igual a: {media_notas:.2f}")