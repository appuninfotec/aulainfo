#3. (Fácil) Soma de 10 números digitados pelo usuário
#Desenvolva um programa que receba 10 números do usuário e imprima a soma de todos eles.


soma = 0  # Inicializa a variável que armazenará a soma
contador = 0  # Inicializa o contador com 0
while contador < 10:  # Executa o loop até que 10 números sejam inseridos
    numero = float(input("Digite um número: "))  # Recebe um número do usuário
    soma += numero  # Adiciona o número à variável soma
    contador += 1  # Incrementa o contador
print("A soma dos números é:", soma)  # Imprime o resultado da soma
