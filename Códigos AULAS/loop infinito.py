contador = 0
#while é enquanto, por exemplo, enquanto o contador for = a 0, execute
#se você não adicionar nada, para que atualize o número do contador, ele fica em loop infinito

#O ponto vermelho serve para usar o debug e deixar o phyton mostrar passo a passo, a gente comanda como que começa
while contador <= 3:
    print("Olá")
    contador += 1
#O while executa primeiro, quando estiver fora do wilhe, continua a execução do código

print(f"Estou fora do while, pois cont = {contador}")