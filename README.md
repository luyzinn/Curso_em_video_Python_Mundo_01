# Curso em video - Python Mundo 01 (www.cursoemvideo.com)
Repositório para os exercícios e desafios do curso de Python - Mundo 01 do Curso em Vídeo!!

<h1> Anotações Importantes </h1>

<h2> Tipos primitivos </h2>

#Comando usado para saber qual o tipo primitivo:,>> type() <<

Str - Stringer - Sempre se refere a palavras. Sempre usado entre aspas 'Olá', '7,5' <br/>
Int - Se é número inteiro 7 , 8 , 10 <br/>
float - Se é número flutuante, que tem . separando, ou seja, se é um número real ex: 5.4 <br/>
Bool - Boleano - Ou True ou False - Quando se refere a valor lógico. Usar sempre Letra maiúscula <br/>

## Ordens de precedência: ##

1 - Parênteses = () <br/>
2 - Potenciaçao = **  <br/>
3 - Multiplicação = *     Divisão = /      Divisão Inteira = //     Resto da Divisão = % <br/>
4 - Adição = +      Subtração = - <br/>

Usando { }, para representar, podemos formatar o texto usando alinhamentos - :<  :>  :^ Ex: {:<20} Ou seja, um espaçamento de 20 com o nome alinhado no meio.  <br/>

:< === Justificado a esquerda / :> Justificado a direita  / :^ Centralizado <br/>
{:.3f} === Especifica que o produto terá 3 casas decimais flutuantes <br/>
,end=' ' === Usado para unir a linha, mesmo com outro comando igual embaixo, como o print! <br/>
\n === Cria uma nova linha, como uma quebra de linha <br/>

n = int(input('Digite um numero: ')) <br/>
Se for usar a variável usar essa linha:  <br/>
s = n + 1 <br/>
a = n - 1 <br/>
print('O sucessor de {} é {} e o antecessor é {}'.format(n, s, a)) <br/>

### Se não for precisar guardar a variavel, é mais fácil usar essa linha abaixo: <br/>
print('O sucessor de {} é {} e o antecessor é {} '.format(n, (n+1), (n-1)))
