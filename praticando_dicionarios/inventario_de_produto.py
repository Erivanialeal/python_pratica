#Implemente um sistema de inventário de produtos, onde:

#O usuário pode adicionar produtos com nome e quantidade.
#dicionario vazio para receber os produtos adicionados
lista_de_produtos = {}
class Inventario:
    @staticmethod
    def adicionar_produto(produto , quantidade):
        #tratando possivel erro, para quer a string fique sempre com letrar minuscula
        produto = produto.lower()
        #convertendo a entrada da variavel entrada para inteiro
        quantidade = int(quantidade)
    
        if produto in lista_de_produtos:
            return f"O produto {produto} já existe no sistema."
        else:
            #adicionando o produto no dicionario
            lista_de_produtos[produto] = quantidade
            return f" Os produtos adicionados são.\n produto: {produto} \n quantidade: {quantidade} \n{lista_de_produtos}"
    #O usuário pode aumentar ou diminuir a quantidade de um produto.
    @staticmethod
    def editar_produto(produto,quantidade):
        if produto in lista_de_produtos:
            lista_de_produtos[produto] = quantidade
            return f"O produto, {produto} teve sua quantidade editada para \n{quantidade} \n {lista_de_produtos}"
        else:
            return f"O produto {produto} mecionado não foi encontrado, essa e a lista de produtos {lista_de_produtos}"
        
    @staticmethod
    def lista():
        if lista_de_produtos:
            return f"Todos os produtos e seus valores {lista_de_produtos}"
    
#O sistema exibe todos os produtos disponíveis e suas quantidades.
#solicitando entrada do usuario
produto=input("Nome do produto:")
quantidade=input("Quantidade do produto:")

inventario=Inventario()
resu=Inventario.adicionar_produto(produto,quantidade)
print(resu)