p = []

for i in range(0,51):
    if i %2==0:
        p.append(i)
    
print(f"A soma dos 50 primeiros números pares é igual a: {sum(p)}")