#7. (Fácil) Soma de n números
#Desenvolva um programa que leia um número n que indica quantos valores devem ser lidos a seguir. Após isso, o usuário deve digitar os números, e o algoritmo deve imprimir a soma de todos eles.


n = int(input("Quantos números você vai digitar? "))  # Recebe o número de valores a serem lidos
soma = 0  # Inicializa a variável que armazenará a soma
contador = 0  # Inicializa o contador com 0
while contador < n:  # Executa o loop até que todos os números sejam inseridos
    numero = float(input("Digite um número: "))  # Recebe um número do usuário
    soma += numero  # Adiciona o número à soma
    contador += 1  # Incrementa o contador
print("A soma dos números é:", soma)  # Imprime o resultado da soma



