# Operações com String no Python. 
# As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find()
# Transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().
''' << Anotaçoes >>
frase[9] -> Pega os caracteres das posições indicadas -- letra E<br/>
frase[9:13] -> Pega os caracteres das posições indicadas -- ENDE<br/>
frase[9:18:2]-> Pega os caracteres das posições indicadas pulando 2 - EDNOA<br/>
len() -> Mostra quantas letras tem a frase -- len(frase) = 38 letras<br/>
count() -> Conta quantas vezes aparece a letra escolhida -- frase.count('s')<br/>
find() -> Procura os caracteres escolhido ------ frase.find('aprendendo')<br/>
replace() -> Troca uma palavra por outra na frase -- frase.replace('python','JavaScript')<br/>
upper() -> Colocar todas as outras letras em maiúsculo -- frase.upper()<br/>
lower() -> Colocar todas as outras letras em minusculo -- frase.lower()<br/>
capilalize() -> Coloca todas a frase em minusculo menos a 1 letra -- frase.capitalize()<br/>
title() -> Todas as palavras começa com letra maiúscula -- frase.title()<br/>
strip() -> Tira o espaço do começo e no fim da frase -- frase.strip()  frase.lstrip()  frase.rstrip()<br/>
split() -> Vai ocorrer uma divisão entre os espaços da frase ----- frase.split()<br/>
.join() -> Juntar uma coisa com a outra -- '-'.join.frase Estou-aprendendo-a-programar-em-python<br/>
'''


frase = 'Curso em vídeo Python'
print(len(frase))
#len = 14
print(frase.count('o'))
#Contou 3 letras 'o'
print(frase.find('deo'))
#Mostrou que ele começou na posiçao 11
print('Curso' in frase)
#Mostrou True - Verdadeiro - Há a palavra na variável frase
print(frase.replace('Curso','Faculdade'))
#Troca a primeira pela segunda palavra ou expressao dentro da variável Str.
print(frase.upper())
#Deixa tudo em maiúsculo
print(frase.lower())
#Deixa tudo em minúsculo
print(frase.capitalize())
#Deixa só a primeira em maiúsculo na frase
print(frase.title())
#Deixa as palavras após o espaço em maiúsculo
frase = '  Aprenda Python  '
print(frase.strip())
#Remove os espaços na frente e após a frase
print(frase.rstrip())
#Remove os espaços na direita(fim)da frase
print(frase.lstrip())
#Remove os espaços na esquerda(frente) da frase

frase = 'Curso em vídeo Python'
print(frase.split())
#Divide a frase em uma lista com os objetos ['Curso', 'em', 'vídeo', 'Python']
div = frase.split()
print(div[0]) #Mostra a posiçao 0 do item da lista .. no caso == ['Curso']

print('--'.join(frase))
#Separa a frase com o indicado no método: C--u--r--s--o-- --e--m-- --v--í--d--e--o-- --P--y--t--h--o--n
