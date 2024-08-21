print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 40

chute = int (input("adivinhe o numero que estou pensando "))

print ("Voce Digitou: ", chute)

if (numero_secreto == chute):
    print("Você Acertou! ")
else:
    print ("Você errou ")


    