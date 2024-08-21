print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 40
total_de_tentativas = 3
while(total_de_tentativas > 0):
    chute = int (input("adivinhe o numero que estou pensando "))
    print ("Voce Digitou: ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if (acertou):
        print("Você Acertou! ")
    elif(maior):
        print ("Você errou, pois o numero que você digitou e maior que o esperado ")
    elif(menor):
        print("Você errou, pois o numero que você digitou e menor que o esperado")

    total_de_tentativas = total_de_tentativas - 1
    