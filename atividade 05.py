#5. (Muito Fácil) Contar quantos números são pares
#Desenvolva um programa que receba 5 números do usuário e, ao final, imprima quantos desses números são pares.


contador = 0  # Inicializa o contador com 0
pares = 0  # Inicializa o contador de números pares com 0
while contador < 5:  # Executa o loop até que 5 números sejam inseridos
    numero = int(input("Digite um número: "))  # Recebe um número do usuário
    if numero % 2 == 0:  # Verifica se o número é par
        pares += 1  # Incrementa o contador de números pares
    contador += 1  # Incrementa o contador geral
print("Quantidade de números pares:", pares)  # Imprime a quantidade de números pares

