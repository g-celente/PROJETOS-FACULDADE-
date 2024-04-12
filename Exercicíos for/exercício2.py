#IMPRIMA TODOS OS NÚMEROS DE 1 A 100 QUE SÃO PARES
p = []

for i in range (1,101):
    if i%2 == 0:
        p.append(i)

print(f"Os números pares são igual a: {p}")