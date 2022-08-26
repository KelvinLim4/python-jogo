def jogar():
    print("***************************************")
    print("** Bem vindo ao jogo da forca! **")
    print("***************************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou  = False

    while(not enforcou and not acertou):

        chute = input("Qual a letra?")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
             print("Encontrei {} na posição {}".format(letra, index))
            index = index + 1

        print("Jogando ...")

    print("Fim do Jogo")

# Variavel interna para execução primaria
if (__name__ == "__main__"):
    jogar()