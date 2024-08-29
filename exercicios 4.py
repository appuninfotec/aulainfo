
#4) Soma de Números
#Desenvolva um programa que receba dez números do usuário e imprima a soma de todos os números digitados.


soma = 0  # Inicia a soma em 0
cont = 0
# Loop que executa 10 vezes
while cont < 10:
    cont = cont + 1
    # Solicita ao usuário que digite um número e converte para inteiro
    numero = int(input("Digite um número: "))
    soma += numero  # Adiciona o número digitado à soma

# Exibe o resultado da soma de todos os números digitados
print(f"A soma dos números digitados é: {soma}")
