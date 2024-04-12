#LER VÁRIAS IDADES E CALCULE A MÉDIA DELAS

quantidade = int(input("Digite quantas notas deseja saber a média: "))
notas = []
soma = 0
media = 0
for i in range(0,quantidade):
    nota = float(input(f'insira a nota {i + 1}: '))
    notas.append(nota)
    soma += nota
    media = soma/len(notas)

print(f'a media foi de: {media} pontos')

  