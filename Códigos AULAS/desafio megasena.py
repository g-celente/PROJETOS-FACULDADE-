#GERAR NÚMEROS ALEATÓRIOS COM PYTHON
import random #biblioteca aleatória 

sorteio = [0,0,0,0,0,0]
aposta = [0,0,0,0,0,0]
i = 0
acertos = []
while i < len(sorteio):
    sorteio[i] =  random.randint(1,60)
    aposta[i] =  int(input(f"Digite o {i+1}° número: "))
    
    if aposta[i] > 60 or aposta[i] < 0:
        print("Número repetido ou inválido, tente novamente....")
        continue
    i +=1

    if aposta in sorteio: 
        acertos.append(aposta[i])

print(f"Os Números Sorteados foram: {sorteio}")
print(f"Os Números Que você Apostou foram: {aposta}")
print(f"No Total, você acertou {len(acertos)} números, que são: {acertos}")

    



    
