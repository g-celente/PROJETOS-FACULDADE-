a = float(input("Digite o valor de a (diferente de zero): "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Calculando o discriminante
delta = b**2 - 4*a*c

# Determinando a natureza das soluções
if delta > 0:
    print("Existem duas raízes reais distintas.")
elif delta == 0:
    print("Existem duas raízes reais iguais.")
else:
    print("Existem duas raízes imaginárias conjugadas.")