def removendo_duplicatas(entrada=[1,2,2,3,4,4,5]): 
    lista_sem_duplicatas = [] #lista vazia para armazer itens que não são duplicados
    for item in entrada: #intera sobre a entrada
        if item not in lista_sem_duplicatas: #verifica se o item já foi adicionado
            lista_sem_duplicatas.append(item) #se não foi ele adiciona
    return lista_sem_duplicatas #retorna a lista com os valores sem duplicatas

resultado=removendo_duplicatas() #Chamando a função
print(resultado)
#saida esperada [1,2,3,4,5]