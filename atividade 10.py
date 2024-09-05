#10. (Normal) Multiplicação de números primos entre 92 e 1478
#Desenvolva um programa que calcule e mostre a multiplicação de todos os números primos entre 92 e 1478.

def eh_primo(n):  # Função que verifica se um número é primo
    if n < 2:  # Números menores que 2 não são primos
        return False
    i = 2  # Inicializa o divisor com 2
    while i * i <= n:  # Executa o loop até que i seja maior que a raiz quadrada de n
        if n % i == 0:  # Verifica se n é divisível por i
            return False  # Retorna False se não for primo
        i += 1  # Incrementa o divisor
    return True  # Retorna True se for primo

produto = 1  # Inicializa a variável que armazenará o produto dos números primos
i = 92  # Inicializa o contador com 92
while i <= 1478:  # Executa o loop até que o contador seja maior que 1478
    if eh_primo(i):  # Verifica se o número atual é primo
        produto *= i  # Multiplica o produto pelo número primo
    i += 1  # Incrementa o contador
print("A multiplicação dos números primos entre 92 e 1478 é:", produto)  # Imprime o resultado do produto
