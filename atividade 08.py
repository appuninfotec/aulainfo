#8. (Fácil) Média de notas com repetição
#Desenvolva um programa que leia as notas da 1ª e 2ª avaliações de um aluno, 
# calcule e imprima a média aritmética desse aluno. 
# Só devem ser aceitos valores válidos (0 a 10) durante a leitura de cada nota. 
# Acrescente uma mensagem 'NOVO CALCULO (S/N)?' para reiniciar ou encerrar o algoritmo.



while True:  # Loop infinito, será encerrado apenas se o usuário não quiser repetir
    nota1 = float(input("Digite a 1ª nota (0 a 10): "))  # Recebe a primeira nota
    while nota1 < 0 or nota1 > 10:  # Verifica se a nota é válida
        nota1 = float(input("Nota inválida! Digite a 1ª nota (0 a 10): "))  # Solicita uma nova nota válida

    nota2 = float(input("Digite a 2ª nota (0 a 10): "))  # Recebe a segunda nota
    while nota2 < 0 or nota2 > 10:  # Verifica se a nota é válida
        nota2 = float(input("Nota inválida! Digite a 2ª nota (0 a 10): "))  # Solicita uma nova nota válida

    media = (nota1 + nota2) / 2  # Calcula a média aritmética das notas
    print("A média do aluno é:", media)  # Imprime a média do aluno

    novo_calculo = input("NOVO CALCULO (S/N)? ").strip().upper()  # Pergunta se o usuário deseja realizar outro cálculo
    if novo_calculo != 'S':  # Verifica se a resposta não é 'S'
        break  # Sai do loop, encerrando o programa
