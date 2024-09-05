print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 40
rodada = 1

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



for rodada in range(1, total_de_tentativas + 1):
    print ("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int (input("adivinhe o numero que estou pensando "))
    print ("Voce Digitou: ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if (acertou):
        print("Você Acertou! ")
        break
    elif(maior):
        print ("Você errou, pois o numero que você digitou e maior que o esperado ")
    elif(menor):
        print("Você errou, pois o numero que você digitou e menor que o esperado")

    rodada = rodada + 1
print("fim do jogo")
    