print("***************************************")
print("** Bem vindo ao jogo de Adivinhação! **")
print("***************************************")

#Definindo numero para comparação
numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas > 0):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite o seu número: ")
    chute = int(chute)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    print("Voce digitou: ", chute)

    if (acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o numero secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que o numero secreto.")

    rodada = rodada + 1

print("Fim do Jogo")
#saber tipo da variavel type(acertou)