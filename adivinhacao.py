print("***************************************")
print("** Bem vindo ao jogo de Adivinhação! **")
print("***************************************")

#Definindo numero para comparação
numero_secreto = 42
#Coletando numero do usuario
chute = input("Digite o seu número: ")
#Convertendo a variavel de string para inteiro
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


print("Fim do Jogo")