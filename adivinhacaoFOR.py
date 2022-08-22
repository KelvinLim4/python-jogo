import random

print("***************************************")
print("** Bem vindo ao jogo de Adivinhação! **")
print("***************************************")

#Definindo numero para comparação
numero_secreto = random.randrange(1,101)
total_de_tentativas = 0

print("Qual o nível de dificuldade? ")
print("(1)Fácil (2)Médio (3)Difícil")

nivel = int(input("Defina o nível: "))

if (nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite um número entre 1 e 100: ")
    chute = int(chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    print("Voce digitou: ", chute)

    if (acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o numero secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que o numero secreto.")


print("Fim do Jogo")
#saber tipo da variavel type(acertou)