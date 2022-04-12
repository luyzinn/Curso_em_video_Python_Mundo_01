#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.


#import random
from random import choice
nome1 = input('Digite o primeiro aluno: ')
nome2 = input('Digite o segundo aluno: ')
nome3 = input('Digite o terceiro aluno: ')
nome4 = input('Digite o quarto aluno: ')
#Para usar o random é necessário usar uma lista
lista = [nome1, nome2, nome3, nome4]
#escolhido = random.choice(lista)
escolhido = choice(lista)


print('O aluno escolhido foi: {}'.format(escolhido))