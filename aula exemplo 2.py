print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 40

chute = int (input("adivinhe o numero que estou pensando "))

print ("Voce Digitou: ", chute)

if (numero_secreto == chute):
    print("Você Acertou! ")
elif(chute > numero_secreto):
    print ("Você errou, pois o numero que você digitou e maior que o esperado ")
elif(chute < numero_secreto):
    print("Você errou, pois o numero que você digitou e menor que o esperado")


    