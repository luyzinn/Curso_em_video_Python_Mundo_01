#Tipos primitivos

#Comando usado para saber qual o tipo primitivo:,>> type() <<

# Str - Stringer - Sempre se refere a palavras. Sempre usado entre aspas 'Olá', '7,5' 
# Int - Se é número inteiro 7 , 8 , 10
# float - Se é número flutuante, que tem . separando, ou seja, se é um número real ex: 5.4
# Bool - Boleano - Ou True ou False - Quando se refere a valor lógico. Usar sempre Letra maiúscula

#Ordens de precedência:

# 1 - Parênteses = ()
# 2 - Potenciaçao = ** 
# 3 - Multiplicação = *     Divisão = /      Divisão Inteira = //     Resto da Divisão = %
# 4 - Adição = +      Subtração = -

#Usando {}, para representar, podemos formatar o texto usando alinhamentos - :<  :>  :^ Ex: {:<20}

# Ou seja, um espaçamento de 20 com o nome alinhado no meio. 
# :< Justificado a esquerda / :> Justificado a direita  / :^ Centralizado
# {:.3f} - Especifica que o produto terá 3 casas decimais flutuantes
# ,end=' ' - Usado para unir a linha, mesmo com outro comando igual embaixo, como o print!
# \n Cria uma nova linha, como uma quebra de linha

n = int(input('Digite um numero: '))
# Se for usar a variável usar essa linha: 
#s = n + 1
#a = n - 1
#print('O sucessor de {} é {} e o antecessor é {}'.format(n, s, a))

# Se não for precisar guardar a variavel, é mais fácil usar essa linha abaixo:
print('O sucessor de {} é {} e o antecessor é {} '.format(n, (n+1), (n-1)))