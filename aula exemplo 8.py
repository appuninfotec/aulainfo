print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 40
rodada = 1
pontos = 1000

print ("Temos quatro niveis escolha um numero para cada niveis")
print ("1 = Fácil")
print ("2 = médio")
print ("3 = Dificil")
print ("4 = infernal")

nivel = int (input("digite qual nivel deseja jogar! "))

if (nivel == 1):
    total_de_tentativas = 20
    print ("nivel escolhido: Fácil")
elif(nivel == 2):
    total_de_tentativas = 10
    print ("nivel escolhido: Médio")
elif(nivel == 3):
    total_de_tentativas = 5
    print ("nivel escolhido: Dificil")
elif(nivel == 4):
    total_de_tentativas = 1
    print ("nivel escolhido: Infernal")

perda_por_tentativa = pontos // total_de_tentativas



for rodada in range(1, total_de_tentativas + 1):
    print ("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int (input("adivinhe o numero que estou pensando "))
    print ("Voce Digitou: ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if acertou:
        print(f"Você Acertou!")
        break
    else:
        pontos -= perda_por_tentativa
        if maior:
            print("Você errou, o número que você digitou é maior que o esperado.")
        elif menor:
            print("Você errou, o número que você digitou é menor que o esperado.")
        
        print(f"Pontos restantes: {pontos}")
        
        if pontos <= 0:
            pontos = 0
            print("Você ficou sem pontos!")
            break


    
    rodada = rodada + 1


print(f"Fim do jogo! Sua pontuação final é: {pontos}") 