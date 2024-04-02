nota =  0 #começa com uma variável menor que 7 para poder entrar no loop
nota = float(input("Digite a nota do aluno:\n"))

#insira o while com a nota para o programa garantir que resolverá 
while nota <= 7 or nota < 0 or nota > 10 :
    nota = float(input("Nota inválida! Digite uma nota maior que 7 e menor que 10: ")) #digite para poder digitar. 
    
print (f" A nota do aluno é {nota}")