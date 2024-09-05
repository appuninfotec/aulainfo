#9. (Normal) Verificar se um número é primo
#Desenvolva um programa que leia um número inteiro qualquer e informe se ele é primo. 
# Um número é dito primo se for divisível apenas por 1 e ele mesmo.


numero = int(input("Digite um número: "))  # Recebe um número do usuário
divisores = 0  # Inicializa a variável que conta os divisores
i = 1  # Inicializa o contador com 1
while i <= numero:  # Executa o loop até que i seja maior que o número
    if numero % i == 0:  # Verifica se i é um divisor do número
        divisores += 1  # Incrementa o contador de divisores
    i += 1  # Incrementa o contador
if divisores == 2:  # Verifica se o número tem exatamente 2 divisores (é primo)
    print(f"{numero} é primo.")  # Imprime que o número é primo
else:
    print(f"{numero} não é primo.")  # Imprime que o número não é primo
