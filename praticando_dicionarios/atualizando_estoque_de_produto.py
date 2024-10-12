estoque_loja={"sabão":3, "arroz":4,"trigo":0,}#lista de dicionario
#função que recebe os paramentros produto,quantidade
def adicionar_produto_ao_estoque(produto,quantidade,):
    #se produto estiver no dicionario estoque_laja
    if produto in estoque_loja:
        #retorne
        return "O produto já existe no estoque."
    #senão
    else:
        #o programa vai acessar o dicionario estoque_loja e vai adicionar a chave produto
        #e o valor quantidade
        estoque_loja[produto] = quantidade
        #retornando o dicionario com todos os produtos inclusive o que foi adicionado
        return estoque_loja
    #aqui mostramos na tela os produtos.
print(adicionar_produto_ao_estoque("camisa" , 10))

def remover_produto_do_estoque():
    produtos_a_remover =[produto for produto,quantidade in estoque_loja.items() if quantidade == 0]
    for produto in produtos_a_remover:
        estoque_loja.pop(produto)
    return f"Produtos removidos {produtos_a_remover}"

def atualizar_quantidade_de_produto(produto,quantidade):
    if produto in estoque_loja:
        if quantidade < 0:
            return "A quantidade não pode ser negativa"
        estoque_loja[produto] = quantidade
        return estoque_loja
    else:
        return "Produto não encontrado no estoque"
print(atualizar_quantidade_de_produto("sabão" , 1))