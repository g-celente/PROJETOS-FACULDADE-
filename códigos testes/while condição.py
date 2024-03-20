cont = 1
notas = 5
soma_notas = 0 
media_sala = 0
#enquanto o contador for menos que notas, executa o código 
while cont <= notas: 
    nota =  float(input(f"Informe a nota: {cont} \n"))
    soma_notas += nota #acumula as notas e faz com que todas que sejam pedidas, somem juntas
    cont += 1
media_sala = soma_notas/notas 
print(f" A média da sala é: {media_sala}") 