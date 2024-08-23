#1) Repetição de Nome
#Escreva um programa que pergunte ao usuário um nome e um número. 
#O programa deve então imprimir o nome na tela repetidamente, 
# o número de vezes que o usuário especificar.


# Solicita ao usuário que digite um nome
nome = input("Digite um nome: ")

# Solicita ao usuário que digite um número e converte para inteiro
numero = int(input("Digite um número: "))

# Loop que executa 'numero' vezes
for i in range(numero):
    # Imprime o nome a cada iteração
    print(nome)
