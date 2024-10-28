#Objetivo:
#Criar uma calculadora modular em Python, usando funções e conceitos de *args e **kwargs
#para realizar operações matemáticas básicas. Essa calculadora permitirá operações com 
#vários números, configuração de precisão para resultados e um histórico das operações
# realizadas.

def calcular(operacao, *args, **kwargs):

    if not args: #verifica se não foram passados números
        return 'Nenhum número passado'
        
    
    if operacao == 'soma':
        resultado = sum(args)

    
    elif operacao == 'subtracao':
        resultado = args[0] #subtração começa com o primeiro número
        for numero in args [1:]:
            resultado -= numero
        
    
    elif operacao == 'multiplicacao':
        resultado = 1 #multiplicação começa com um
        for numero in args:
            resultado *= numero

       
    
    elif operacao == 'divisao':
        resultado = args[0] #Divisão começã com o primeiro número

        for numero in args [1:]:
            if numero == 0:
                return 'Erro: Divisão por zero'
            resultado /= numero

    else:
        return 'Operação inválida'

    precisao= kwargs.get('precisao', 2)  
    return round(resultado, precisao )

def main():
    #solicita a operação desejada.
    operacao = input("Digite a operação desejada. (Soma, Subtração, Multiplicação, Divisão.)").lower()

    numeros= input('Digite os números separados por espaço.').split()
    numeros =[float(num) for num in numeros] #corrige a conversão para float

    resultado=calcular(operacao,*numeros)
    print('Resultado:',resultado)
main()

        
