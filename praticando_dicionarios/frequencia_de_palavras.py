def frequencia_palavras(texto):
    #converter o texto para uma lista de palavras,separando por espaços
    palavras= texto.split()
    #iniciando um dicionario vazio para armazenar a frequencia
    frequencia={}
    #interando sobre cada palavras na lista.
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra]+=1
            #caso contrario adiciona a palavra ao dicionario com valor 1
        else:
            frequencia[palavra]=1

    return frequencia
texto="gato cachorro gato"
resultado =frequencia_palavras(texto)
print(resultado)
