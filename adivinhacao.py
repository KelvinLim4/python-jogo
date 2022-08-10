print("***************************************")
print("** Bem vindo ao jogo de Adivinhação! **")
print("***************************************")

#Definindo numero para comparação
numero_secreto = 42

#Coletando numero do usuario
chute = input("Digite o seu número: ")

#Convertendo a variavel de string para inteiro
chute = int(chute)

print("Voce digitou: ", chute)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim do Jogo")