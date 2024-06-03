def cadastrar_pessoas():
    pessoas = []
    while True:
        try:
            nome = input("Nome: ")
            cpf = input("CPF: ")
            idade = int(input("Idade: "))
            renda_mensal = float(input("Renda Mensal: "))
        except:
            print("Informação inválida, tente novamente...")
            continue

        pessoa = [nome, cpf, idade, renda_mensal]
        pessoas.append(pessoa)
        
        continuar = input("Deseja cadastrar mais uma pessoa? (s/n): ").lower()

        if continuar == 'n':
            return pessoas     
        elif continuar == 's':
            continue
        else:
            print("Opção inválida, tente novamente...")
            continue
        

def print_pessoas(pessoas):       
    for pessoa in pessoas:
        print(pessoa)

def multiply (pessoas):
    soma_idades = 0
    soma_renda = 0
    
    for pessoa in pessoas:
        soma_idades += pessoa[2]
        soma_renda += pessoa[3]

    media_idade = soma_idades / len(pessoas)
    media_renda = soma_renda / len(pessoas)
    
   
    print(f"Média de idade: {media_idade:.2f}")
    print(f"Média de renda mensal: {media_renda:.2f}")


pessoas = cadastrar_pessoas()
print_pessoas(pessoas)
multiply(pessoas)