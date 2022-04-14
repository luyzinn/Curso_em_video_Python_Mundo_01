''' Desafio 26
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma frase: ')).strip().upper()
cont_a = frase.count('A')
posi_a_ini = frase.find('A') + 1 # para aparecer na posiçao que estamos lendo(Eliminando a posiçao 0)
posi_a_final = frase.rfind('A') + 1 # rfind para procurar a ultima ocorrencia
print('A sua frase tem {} letras ''A''. A primeira ocorre na posiçao {} e a útilma na posiçao {}.'.format(cont_a, posi_a_ini,posi_a_final))