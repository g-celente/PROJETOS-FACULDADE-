#pokemons = ["picachu", "charizard", "bubbasauro"]

#numeros = [1, 2 , 3 , 4 , 5 ] #o vetor é como ter um tamanho pré definido, fixo e da mesmo atributo 

#p = [] #já assim, você consegue adicionar ou mudar os valores aqui dentro, somar e etc... 
#indice = 0 
#while indice < len(pokemons):
    #print(pokemons[indice])
    #indice += 1

#você pode usar o len(pokemons) para ele ditar a quantidade de itens que tem dentro da lista

#pokemons[0] = #picachu, isso você consegue acessar um item dentro do vetor
#pokemons[0] = int(input("Digite o primeiro pokemon")) #Isso serve para quando eu quiser que o usuário
#digite o pokemon na posição dentro do vetor

#PRATICANDO AGORA
#Criar um vetor com números, printar o vetor e cada número la dentro
numeros = [5,7,12,2,9,21]
i = 0
while i < len(numeros): #aqui você usa o while i < len(numeros), faz com que o while continue até o i ser
#igual a quantidade de elementos dentro do vetor
    print(numeros[i])
    i += 1

#SUBSTITUIÇÃO DE VALORES NO VETOR 
numeros[1] = 17 
numeros[2] = 22 
print(40*"-")
print(f"O novo numero do 1 = {numeros[1]}")
print(f"O novo numero do 2 = {numeros[2]}")
numeros[2] = 1
numeros[4] = 29
print(f"O novo numero 3 = {numeros[2]}")
print(f"O novo numero 5 = {numeros[4]}")

print(numeros)
