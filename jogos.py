import forca
import adivinhacaoFOR

def escolha_jogo():
    print("***************************************")
    print("********* Escolha o seu jogo! *********")
    print("***************************************")


    print("(1)Forca (2)Advinhação")

    jogo = int(input("Qual jogo: "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacaoFOR.jogar()

# Variavel interna para controlar execução
if (__name__ == "__main__"):
    escolha_jogo()