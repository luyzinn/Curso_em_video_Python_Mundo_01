#Ordens de precedência:
# 1 - Parênteses = ()
# 2 - Potencial = ** 
# 3 - Multiplicação = *     Divisão = /      Divisão Inteira = //     Resto da Divisão = %
# 4 - Adição = +      Subtração = -

#Usando {}, para representar, podemos formatar o texto usando alinhamentos - :<  :>  :^ Ex: {:<20}
# Ou seja, um espaçamento de 20 com o nome alinhado no meio. 
# :< Justificado a esquerda / :> Justificado a direita  / :^ Centralizado
# {:.3f} - Especifica que o produto terá 3 casas decimais flutuantes
# ,end=' ' - Usado para unir a linha, mesmo com outro comando igual embaixo, como o print!
# \n Cria uma nova linha, como uma quebra de linha

print ('== DESAFIO 05 ==')
n = int(input('Digite um numero: '))
# Se for usar a variável usar essa linha: 
#s = n + 1
#a = n - 1
#print('O sucessor de {} é {} e o antecessor é {}'.format(n, s, a))

# Se não for precisar guardar a variavel, é mais fácil usar essa linha abaixo:
print('O sucessor de {} é {} e o antecessor é {} '.format(n, (n+1), (n-1)))
