
#aqui imprime na tela o cabeçalho
print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')


numero_secreto = 40 #aqui é criado a variável numero secreto e é atribuido um valor 40 a ela
total_de_tentativas = 3 #aqui é criado a variável Numero de tentativas e é atribuido um valor 3 a ela, pois e ela quem vai parar o fluxo quando as tentativas acabarem
total_de_tentativas2 = 3 #aqui é criado a variável Numero de tentativas2 e é atribuido um valor 3 a ela, pois e ela quem vai somente mostrar a quantidade de tentativas que o usúario pode tentar

rodada = 1 #aqui é criado a variável rodada e é atribuido um valor 1 a ela, ao contrario de total_de_tentativas2 ela vai somente mostrar em qual tentativa o usuario ta chutando o numero

while(total_de_tentativas > 0 ): #aqui começa o laço while (ou no portugou Enquanto). Logo enquanto o total_de_tentativas é maior que zero o laço vai ficar um um loop. 
    
    print ("Tentativa {} de {}".format(rodada, total_de_tentativas2)) #aqui será mostrado na tela o numero de tentativas que o usuario esta atraves da variável rodada e quantas tentativas ele pode jogar atraves da variável total_de_tentativas2.
 
    chute = int (input("adivinhe o numero que estou pensando ")) #aqui cria a variável chute e ela recebe o valor que o cliente digitar atravez do input
    print ("Voce Digitou: ", chute) #aqui ele mostra na tela qual foi o numero digitado
    
    acertou = chute == numero_secreto #aqui criei uma variável acertou e dei o valor a ela com a condição que a variável chute seja identico aou numero_secreto
    maior = chute > numero_secreto # #aqui criei uma variável maior e dei o valor a ela com a condição que a variável chute seja maior aou numero_secreto
    menor = chute < numero_secreto # #aqui criei uma variável maior e dei o valor a ela com a condição que a variável chute seja menor aou numero_secreto


    if (acertou): # aqui inicia o if (SE) com a condição se a variável acertou for verdadeira ele vai mostrar na tela que acertou e parara o programa
        print("Você Acertou! ")
        break # se o usuário acertar o numero secreto ele sai do laço while e passa para o final mostrando que esta no fim do jogo
    elif(maior): # aqui e uma negação ao if (não se) se a condição maior for verdadeira ele vai mostrar que errou mas que o numero digitado e maior que o numero secreto
        print ("Você errou, pois o numero que você digitou e maior que o esperado ")
    elif(menor): # aqui e uma negação ao if (não se) se a condição maior for verdadeira ele vai mostrar que errou mas que o numero digitado e menor que o numero secreto
        print("Você errou, pois o numero que você digitou e menor que o esperado")

    rodada = rodada + 1 #aqui ele acrescenta sempre mais um na contagem da variavel rodada para que cada tentativa ele mostre o valor da rodada somandao +1
    total_de_tentativas = total_de_tentativas - 1 # aqui ele vai fazer um decrescimo no numero de tentativas para cada rodada assim quando chegar a zero vai atingir a condição de parada do laço while (enquanto)
print("fim do jogo") #aqui mosta na tela que o jogo acabou
    