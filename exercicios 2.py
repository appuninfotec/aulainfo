
#2) Sequências com Loop while
#Crie um programa que imprima três sequências diferentes de números usando um loop while:

#Sequência 1: Imprimir todos os números pares de 2 a 20.
#Sequência 2: Imprimir todos os múltiplos de 5 de 50 até 5, em ordem decrescente.
#Sequência 3: Imprimir os primeiros 10 números da sequência dos quadrados perfeitos (1, 4, 9, 16, 25, 36, 49, 64, 81, 100).


# Sequência 1: Números pares de 2 a 20
print("Sequência 1:")
i = 2  # Inicia o contador em 2
while i <= 20:  # Continua enquanto i for menor ou igual a 20
    print(i, end=", ")  # Imprime o número e mantém a impressão na mesma linha
    i += 2  # Incrementa i em 2 a cada iteração
print()  # Quebra de linha após a sequência

# Sequência 2: Múltiplos de 5 de 50 até 5
print("Sequência 2:")
i = 50  # Inicia o contador em 50
while i >= 5:  # Continua enquanto i for maior ou igual a 5
    print(i, end=", ")  # Imprime o número e mantém a impressão na mesma linha
    i -= 5  # Decrementa i em 5 a cada iteração
print()  # Quebra de linha após a sequência

# Sequência 3: Quadrados perfeitos de 1 a 10
print("Sequência 3:")
i = 1  # Inicia o contador em 1
while i <= 10:  # Continua enquanto i for menor ou igual a 10
    print(i**2, end=", ")  # Imprime o quadrado de i e mantém na mesma linha
    i += 1  # Incrementa i em 1 a cada iteração
print()  # Quebra de linha após a sequência