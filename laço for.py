print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 40
# Define o número secreto que o jogador terá que adivinhar, no caso, 40

total_de_tentativas = 3
# Define o número total de tentativas que o jogador terá, no caso, 3 tentativas

rodada = 1
# Inicializa a variável rodada com o valor 1, que será usada para acompanhar em qual rodada o jogador está

for rodada in range(1, total_de_tentativas + 1):
    # Um loop for que será repetido de 1 até o total de tentativas (inclusive)
    # O 'total_de_tentativas + 1' é para incluir a terceira tentativa, pois o range exclui o número final

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    # Imprime a mensagem com o número da tentativa atual e o número total de tentativas

    chute = int(input("adivinhe o numero que estou pensando "))
    # Solicita ao usuário que insira um número (seu "chute") e converte a entrada de string para inteiro

    print("Voce Digitou: ", chute)
    # Imprime o número que o usuário digitou

    acertou = chute == numero_secreto
    # Verifica se o chute do usuário é igual ao número secreto (acertou)
    
    maior = chute > numero_secreto
    # Verifica se o chute do usuário é maior que o número secreto
    
    menor = chute < numero_secreto
    # Verifica se o chute do usuário é menor que o número secreto

    if (acertou):
        # Se o jogador acertou:
        print("Você Acertou! ")
        # Imprime a mensagem de acerto
        break
        # Interrompe o loop, pois o jogador adivinhou corretamente
    elif (maior):
        # Se o chute foi maior que o número secreto:
        print("Você errou, pois o numero que você digitou e maior que o esperado")
        # Imprime uma mensagem dizendo que o chute foi maior
    elif (menor):
        # Se o chute foi menor que o número secreto:
        print("Você errou, pois o numero que você digitou e menor que o esperado")
        # Imprime uma mensagem dizendo que o chute foi menor

    rodada = rodada + 1
    # Incrementa a rodada em 1, embora neste código o valor não seja utilizado, já que o loop for controla a variável rodada

print("fim do jogo")
# Quando o loop termina (seja por acerto ou por esgotamento das tentativas), imprime "fim do jogo"