#11. (Divertido) Jogo de Adivinhação
#Vamos criar um jogo simples onde o computador escolhe um número entre 1 e 10, e 
#o usuário tem que adivinhar qual é o número. O jogo só termina quando o usuário acertar!


import random  # Importa o módulo random para gerar números aleatórios
numero_secreto = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10
acertou = False  # Inicializa a variável de controle como False

while not acertou:  # Executa o loop até que o usuário acerte o número
    palpite = int(input("Tente adivinhar o número (entre 1 e 10): "))  # Recebe o palpite do usuário
    if palpite == numero_secreto:  # Verifica se o palpite está correto
        print("Parabéns! Você acertou!")  # Imprime mensagem de acerto
        acertou = True  # Define a variável de controle como True, encerrando o loop
    else:
        print("Tente novamente!")  # Imprime mensagem de erro e repete o loop

