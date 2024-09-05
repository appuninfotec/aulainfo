#4. (Fácil) Soma da metade de 10 números
#Desenvolva um programa que receba 10 números e imprima a soma da metade de todos os números digitados.



soma = 0  # Inicializa a variável que armazenará a soma das metades
contador = 0  # Inicializa o contador com 0
while contador < 10:  # Executa o loop até que 10 números sejam inseridos
    numero = float(input("Digite um número: "))  # Recebe um número do usuário
    soma += numero / 2  # Adiciona a metade do número à variável soma
    contador += 1  # Incrementa o contador
print("A soma da metade dos números é:", soma)  # Imprime o resultado da soma


