import random

def jogar():
    print("***************************************")
    print("** Bem vindo ao jogo da forca! **")
    print("***************************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou  = False
    erros = 0

    print(letras_acertadas)

    #while = condição
    #Enquanto nao enforcou e nao acertou = jogue
    while(not enforcou and not acertou):

        chute = input("Qual a letra?")
        #.strip remove espaços
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            #para verificar cada letra dentro da palavra
            for letra in palavra_secreta:
                #.upper Converte os caracteres minúsculos de uma cadeia de caracteres em maiúsculo
                if(chute.upper() == letra.upper()):
                    #alimentando o vetor
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou ^^")
    else:
        print("Você perdeu :(")



# Variavel interna para execução primaria
if (__name__ == "__main__"):
    jogar()