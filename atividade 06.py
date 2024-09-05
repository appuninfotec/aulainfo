#6. (Muito Fácil) Série harmônica
#Desenvolva um programa que leia um valor n, inteiro e positivo, e calcule a série harmônica:

#S = 1 + 1/2 + 1/3 + ... + 1/n



n = int(input("Digite o valor de n: "))  # Recebe o valor de n do usuário
soma = 0  # Inicializa a variável que armazenará a soma da série harmônica
i = 1  # Inicializa o contador com 1
while i <= n:  # Executa o loop até que o contador seja maior que n
    soma += 1 / i  # Adiciona o termo 1/i à soma
    i += 1  # Incrementa o contador
print("A soma da série harmônica é:", soma)  # Imprime o resultado da soma