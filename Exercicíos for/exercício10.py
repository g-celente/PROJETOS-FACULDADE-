lista =  [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
numero_freq = 0

for numero in lista:
    if lista.count(numero) > numero_freq:
        repeticoes = lista.count(numero)
        numero_freq = numero

print(f"O número que mais se repete é igual a: {numero_freq} com {repeticoes} repetições ")