# Curso em video - Python Mundo 01 (www.cursoemvideo.com)
*Repositório para os exercícios e desafios do curso de Python - Mundo 01 do Curso em Vídeo!!*

<h2> Anotações Importantes </h2>

### Tipos primitivos

<h3>Comando usado para saber qual o tipo primitivo: *,type( )* </h3>

*Str* - Stringer - Sempre se refere a palavras. Sempre usado entre aspas 'Olá', '7,5' <br/>
*Int* - Se é número inteiro 7 , 8 , 10 <br/>
*float* - Se é número flutuante, que tem . separando, ou seja, se é um número real ex: 5.4 <br/>
*Bool* - Boleano - Ou True ou False - Quando se refere a valor lógico. Usar sempre Letra maiúscula <br/>

### Ordens de precedência: ##

1 - Parênteses = () <br/>
2 - Potenciaçao = **  <br/>
3 - Multiplicação = *     Divisão = /      Divisão Inteira = //     Resto da Divisão = % <br/>
4 - Adição = +      Subtração = - <br/>

**Usando { }, para representar, podemos formatar o texto usando alinhamentos - :<  :>  :^ Ex: {:<20} Ou seja, um espaçamento de 20 com o nome alinhado no meio.** <br/>

*:<* == Justificado a esquerda / :> Justificado a direita  / :^ Centralizado <br/>
*{:.3f}* == Especifica que o produto terá 3 casas decimais flutuantes <br/>
*,end=' '* == Usado para unir a linha, mesmo com outro comando igual embaixo, como o print! <br/>
*\n* == Cria uma nova linha, como uma quebra de linha <br/>

n = int(input('Digite um numero: ')) <br/>
Se for usar a variável usar essa linha:  <br/>
s = n + 1 <br/>
a = n - 1 <br/>
print('O sucessor de {} é {} e o antecessor é {}'.format(n, s, a)) <br/>

Se não for precisar guardar a variavel, é mais fácil usar essa linha abaixo: <br/>
print('O sucessor de {} é {} e o antecessor é {} '.format(n, (n+1), (n-1)))

### Módulos<br/>

Para importar módulos completos usamos:<br/>
*Import Módulo completo* - Ex: **import match** <br/>
*Para ferramenta específica do módulo* - Ex: **from math import ceil**<br/>



### Extra:  ***Comandos mais usados no Git/Gitub***

git status - Verificar status da pasta e arquivos<br/>
git add . - adicionar o repositorio local<br/> 
git commit -m " " - Escrevar um commit ou comentário sobre a versao a ser adicionada<br/>
git push origin main - Fazer push e enviar arquivos para o github<br/>
git pull - Git pull -Se você estiver no seu ambiente de trabalho e quiser atualizar a branch que está trabalhando!<br/>


### Manipulando Textos 

                 frase = 'ESTOU APRENDENDO A PROGRAMAR EM PYHTON' 

[   ] -> Símbolo de indice (listas)

frase[9] -> Pega os caracteres das posições indicadas -- letra E<br/>
frase[9:13] -> Pega os caracteres das posições indicadas -- ENDE<br/>
frase[9:18:2]-> Pega os caracteres das posições indicadas pulando 2 - EDNOA<br/>
len() -> Mostra quantas letras tem a frase -- len(frase) = 38 letras<br/>
count() -> Conta quantas vezes aparece a letra escolhida -- frase.count('s')<br/>
find() -> Procura os caracteres escolhido e mostra a posiçao - frase.find('aprendendo')<br/>
rfind() -> Procura os caracteres escolhido a direita.. ou seja o ultimo - frase.find('aprendendo')<br/>
replace() -> Troca uma palavra por outra na frase -- frase.replace('python','JavaScript')<br/>
upper() -> Colocar todas as outras letras em maiúsculo -- frase.upper()<br/>
lower() -> Colocar todas as outras letras em minusculo -- frase.lower()<br/>
capilalize() -> Coloca todas a frase em minusculo menos a 1 letra -- frase.capitalize()<br/>
title() -> Todas as palavras começa com letra maiúscula -- frase.title()<br/>
strip() -> Tira o espaço do começo e no fim da frase -- frase.strip()  frase.lstrip()  frase.rstrip()<br/>
split() -> Vai ocorrer uma divisão entre os espaços da frase ----- frase.split()<br/>
.join() -> Juntar uma coisa com a outra -- '-'.join.frase Estou-aprendendo-a-programar-em-python<br/>


