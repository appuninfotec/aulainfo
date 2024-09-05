#aqui eu criei um cabeçalho para o jogo
print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

#aqui estou criando a variavel e numero secreto e dando um valor para ela
numero_secreto = 40

#aqui estou começão o jogo pedindo para o usuario digitar um numero para adicionar a variavel chute
chute = int (input("adivinhe o numero que estou pensando "))

#aqui estou pedindo ao jogo para mostrar o valor digitado
print ("Voce Digitou: ", chute)

#aqui sera uma comparação entre o numero digitado e o numero secreto que anteriormente ja informei no codigo
if (numero_secreto == chute):
    #aqui mostra o resutado se verdadeiro
    print("Você Acertou! ")
else:
    #aqui mostra o resultado se for falso
    print ("Você errou ")


    