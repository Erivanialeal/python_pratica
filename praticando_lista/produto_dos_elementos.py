def produto(entrada=[2,3,4]): 
  resultado = 1 #resultado começa com 1 para não dá erro na multiplicação
  for item in entrada:
    resultado = resultado * item
        
  return resultado
    
re=produto()
print(re)

#saida experada 24
    
