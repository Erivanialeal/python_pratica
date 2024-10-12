# Tradução de Palavras
#Crie um dicionário que mapeia palavras de um idioma para outro
palavras = {'amor':'love', 'azul': 'blue', 'arroz':'rice',}
#Permitir ao usuário adicionar novas traduções.
def novas_traducoes(nova_palavra,traducao):
    #matendo o padrao das letras
    try:
        nova_palavra = nova_palavra.lower()
        traducao = traducao.lower()
        #vendo se a nova palavra esta no dicionario 
        if nova_palavra in palavras:
            return f'A tradução da palavra {nova_palavra} já existe, porfavor digite uma nova palavra.'
        #se não estiver a nova palavra será adicionada no dicionario
        else:
            palavras[nova_palavra] = traducao
        return f'A tradução da palavra {nova_palavra} para o ingles é {traducao} '
    except Exception as e:
        return "Erro ao adicionar a traduçõa"

#Permitir ao usuário buscar a tradução de uma palavra.
def buscar_traducao(palavra):
    try:
        #mantendo o padrao das letras
        palavra = palavra.lower()
        #se a palavra buscada estiver no dicionario o programa retornara a sua tradução
        if palavra  in palavras:
            return f' A tradução da palavra {palavra} é {palavras[palavra]}'
        #se não estiver...
        else:
            return f'Nenhuma tradução encontrada'
    except Exception as e:
        return "Ocorreu um erro ao buscar tradução."
    
#Exibir todas as traduções cadastradas.
def traducoes_cadastradas():
    try:
        #vendo a lista de palavras cadastradas
        if palavras:
            return f'As traduções das palavras registradas são: {palavras}'
        #caso não tiver nenhuma palavra em palavras o programa retorna uma mensagem de aviso.
        else:
            return 'Tradução  não cadastrada.'
    except Exception as e:
        return 'Erro ao exibir  tradução.'
try:   
    
    #buscando entrada do usuario
    nova_palavra = input('Adicionar nova palavra:')
    traducao = input('Tradução da palavra:')
    print(novas_traducoes(nova_palavra,traducao)) #chamando as funções

    palavra_para_buscar = input('Buscar tradução para a palavra:')
    print(buscar_traducao(palavra_para_buscar)) #chamando a função

    print(traducoes_cadastradas()) #chamando a função.
except Exception as e:
    print(f'Ocorreu um erro durante a execução do programa {e}')