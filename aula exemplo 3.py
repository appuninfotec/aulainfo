#aqui eu criei um cabeçalho para o jogo

print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

#aqui estou criando a variavel e numero secreto e dando um valor para ela
numero_secreto = 40
#aqui estou criando a variavel total de tentativas e dando um valor para ela
total_de_tentativas = 3

#aqui estou usando um laço "enquanto" logo nquanto a variavel for maior que zero o codigo vai continuar funcionando e pedindo ao usuario apra digitar
while(total_de_tentativas > 0):
    chute = int (input("adivinhe o numero que estou pensando "))
    print ("Voce Digitou: ", chute)

#aqui estou criando umas variaveis e ja atribuindo condições a elas
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

#aqui aqui vai ser as comparações veradeiro ou falso das variaveis criadas
    if (acertou):
        print("Você Acertou! ")
    elif(maior):
        print ("Você errou, pois o numero que você digitou e maior que o esperado ")
    elif(menor):
        print("Você errou, pois o numero que você digitou e menor que o esperado")
#aqui enquanto total de tentativas sempre vai subtrair de - 1 para poder chegar a zero e nao atender a condição de maior que zero fazendo assim o codigo sair do loop
    total_de_tentativas = total_de_tentativas - 1
    