#3) Contador de Passos
#Escreva um programa que simule um contador de passos. 
# O programa deve começar com o contador em 0 e, em cada iteração do while, 
# deve adicionar um número aleatório de 1 a 5 ao contador. 
# O loop deve continuar até que o contador alcance ou ultrapasse 100 passos. 
# O programa então exibe o número total de iterações necessárias para atingir ou ultrapassar os 100 passos.



import random  # Importa o módulo random para gerar números aleatórios

contador = 0  # Inicia o contador de passos em 0
iteracoes = 0  # Inicia o contador de iterações em 0

# Continua o loop até que o contador de passos seja maior ou igual a 100
while contador < 100:
    qtd_aleatorio = random.randint(1, 5)  # Gera um número aleatório entre 1 e 5
    contador += qtd_aleatorio  # Adiciona o número aleatório ao contador de passos
    iteracoes += 1  # Incrementa o contador de iterações

# Exibe o número total de iterações necessárias para atingir 100 passos
print(f"Total de iterações necessárias: {iteracoes}")
