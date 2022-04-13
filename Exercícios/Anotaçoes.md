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

# Manipulando Textos 

  frase = 'ESTOU APRENDENDO A PROGRAMAR EM PYHTON'

  [] -> Símbolo de indice (listas)

  frase[9] -> Pega os caracteres das posições indicadas -- letra E
  frase[9:13] -> Pega os caracteres das posições indicadas -- ENDE
  frase[9:18:2]-> Pega os caracteres das posições indicadas pulando 2 - EDNOA
  len() -> Mostra quantas letras tem a frase -- len(frase) = 38 letras
  count() -> Conta quantas vezes aparece a letra escolhida -- frase.count('s')
  find() -> Procura os caracteres escolhido ------ frase.find('aprendendo')
  replace() -> Troca uma palavra por outra na frase -- frase.replace('python','JavaScript')
  upper() -> Colocar todas as outras letras em maiúsculo -- frase.upper()
  lower() -> Colocar todas as outras letras em minusculo -- frase.lower()
  capilalize() -> Coloca todas a frase em minusculo menos a 1 letra -- frase.capitalize()
  title() -> Todas as palavras começa com letra maiúscula -- frase.title()
  strip() -> Tira o espaço do começo e no fim da frase -- frase.strip()  frase.lstrip()  frase.rstrip()
  split() -> Vai ocorrer uma divisão entre os espaços da frase ----- frase.split()
  .join() -> Juntar uma coisa com a outra -- '-'.join.frase Estou-aprendendo-a-programar-em-python

