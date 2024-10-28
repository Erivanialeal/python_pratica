#Desafio 1: Função de Média
#Crie uma função chamada calcular_media que aceita um número variável de argumentos
#  e retorna a média deles. Use *args para receber os números.

def calcular_media(*notas):
    soma = sum(notas)
    quantidade = len(notas)
    media = soma / quantidade
    return media
notas_input=input("Notas:")
notas = [float(nota) for nota  in notas_input.split()]#converte a entrada em uma lsita de float
media=calcular_media(*notas)
print(f'A nota da media é {media:.2f}')
