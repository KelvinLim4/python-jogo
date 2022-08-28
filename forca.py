def jogar():
    print("***************************************")
    print("** Bem vindo ao jogo da forca! **")
    print("***************************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou  = False

    #while = condição
    #Enquanto nao enforcou e nao acertou = jogue
    while(not enforcou and not acertou):

        chute = input("Qual a letra?")
        #.strip remove espaços
        chute = chute.strip()

        index = 0
        #para verificar cada letra dentro da palavra
        for letra in palavra_secreta:
            #.upper Converte os caracteres minúsculos de uma cadeia de caracteres em maiúsculo
            if(chute.upper() == letra.upper()):
             print("Encontrei {} na posição {}".format(letra, index))
            index = index + 1

        print("Jogando ...")
    print("Fim do Jogo")

# Variavel interna para execução primaria
if (__name__ == "__main__"):
    jogar()