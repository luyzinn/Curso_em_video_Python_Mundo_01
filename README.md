# Curso em video - Python Mundo 01 (www.cursoemvideo.com)
*Repositório para os exercícios e desafios do curso de Python - Mundo 01 do Curso em Vídeo!!*

<h2> Anotações Importantes </h2>
<br/>

### Tipos primitivos: <br>

**Comando usado para saber qual o tipo primitivo: ,type( )**

*Str* - Stringer - Sempre se refere a palavras. Sempre usado entre aspas 'Olá', '7,5' <br/>
*Int* - Se é número inteiro 7 , 8 , 10 <br/>
*float* - Se é número flutuante, que tem . separando, ou seja, se é um número real ex: 5.4 <br/>
*Bool* - Boleano - Ou True ou False - Quando se refere a valor lógico. Usar sempre Letra maiúscula <br/>

### Ordens de precedência:

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
*print('O sucessor de {} é {} e o antecessor é {} '.format(n, (n+1), (n-1)))*

<p>
Para descobrir se um número é par:<br/>
número % 2 == 0:<br/>
print('Seu número é par!')<br/>
</p>

### Módulos 
<br/>

**Para importar módulos completos usamos:**
<br/>

*Import Módulo completo* - Ex: **import match** <br/>
*Para ferramenta específica do módulo* - Ex: **from math import ceil**<br/>

*from random import randint* Usar nesse caso a linha randint (0,5)<br/>

import random - Usar para a função randrage( escolher qual o range..o começo é zero..escolher apenas o número o qual ele deve ir)<br/>

**from time import sleep** <br/>
função do módulo time que faz o computador 'dormir' ou esperar um determinado tempo para prosseguir o algoritimo

<br/>

**Módulo para saber a data atual**


from datetime import date<br/>
ano = date.today().year
<br/>

**Para descobrir o menor e maior valor de uma lista ou variável:**
>.format(min(n1,n2,n3))) <br/>
>.format(max(n1,n2,n3))) 

<br/>

### Extra:  ***Comandos mais usados no Git/Gitub***
<br/>
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
<br/>
split() -> Vai ocorrer uma divisão entre os espaços da frase ----- frase.split()<br/>
<p>
Exemplo: frase = 'Curso em vídeo Python'<br/>
print(frase.split()) - Divide a frase em uma lista com os objetos ['Curso', 'em', 'vídeo', 'Python']<br/>
div = frase.split()<br/>
print(div[0]) - *Mostra a posiçao 0 do item da lista .. no caso == ['Curso']*<br/>
</p>
.join() -> Juntar uma coisa com a outra -- '-'.join.frase Estou-aprendendo-a-programar-em-python<br/>

<<<<<<< HEAD
### Condicionais IF e ELSE

*variável* = int(input('Quantos anos seu carro tem? '))
if *variável* >=3: *A condiçao vem antes dos :*
    print('Seu carro é velho')
else: *Nao esquecer dos :*
    print('Seu carro é novo')
>> Aqui temos uma condicional composta!



=======
### Cores no terminal

Sempre usar \033[ a partir daí o primeiro número é o estilo .. Exemplo:

\033[0 - none .. sem estilo <br>
\033[1 - Negrito <br>
\033[4 - Subilinhado<br>
\033[7 - Negativo .. alternar fundo e frente

Segundo número é a cor - ( Sempre separados por ponto e vírgula ; )

\033[0;30 - Preto

Ver tabela abaixo:

text        ..        background
 
30  ..    black       preto          40<br>
31  ..    red           vermelho   41<br>
32  ..    green       verde         42<br>
33  ..    yellow      amarelo    43<br>
34  ..    blue          azul           44<br>
35  ..    Magenta  Magenta  45<br>
36  ..    cyan         ciano         46<br>
37  ..    grey          cinza         47<br>
97  ..    white        branco     107<br>




             Cores Normais

         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'branco':'\033[30m',
         'roxo':'\033[35m',
         'verde':'\033[32m',
         'ciano':'\033[36m',
         'limpa':'\033[m',
         'preto e branco':'\033[7;30;m',

                cores em negrito

         'vermelho em negrito':'\033[1;31m',
         'azul em negrito':'\033[1;34m' ,
         'amarelo em negrito':'\033[1;33m' ,
         'branco em negrito':'\033[1;30m',
         'roxo em negrito':'\033[1;35m',
         'verde em negrito':'\033[1;32m',
         'ciano em negrito':'\033[1;36m',

               cores sublinhadas

         'vermelho sublinhado':'\033[4;31m',
         'azul sublinhado':'\033[4;34m',
         'amarelo sublinhado':'\033[4;33m',
         'branco sublinhado':'\033[4;30m',
         'roxo sublinhado':'\033[4;35m',
         'verde sublinhado':'\033[4;32m',
         'ciano sublinhado':'\033[4;36m'

Exemplo final: 

print('\033[4;30;45m  Olá Mundo  \033[m')

Olá mundo simples com fundo roxo;
         

