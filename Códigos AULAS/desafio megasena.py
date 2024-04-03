#GERAR NÚMEROS ALEATÓRIOS COM PYTHON
import random #biblioteca aleatória 
p = []
sorteio = [0,0,0,0,0,0]
aposta = [0,0,0,0,0,0]
i = 0
while i < len(sorteio):
    sorteio[i] =  random.randint(1,60)
    aposta[i] =  int(input(f"Digite o {i+1}° número: "))
    i +=1
    if aposta == sorteio :
        p.append(aposta)

print (f"O valor sorteado é igual a: {sorteio}")
print (f"A sua aposta deu: {aposta}")
print(f"Os números que você acertou foram: {p}")
