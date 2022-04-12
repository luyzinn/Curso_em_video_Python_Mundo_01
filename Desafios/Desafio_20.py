#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#import random 
from random import shuffle

aluno1 = input('Digite o primeiro aluno: ')
aluno2 = input('Digite o segundo aluno: ')
aluno3 = input('Digite o terceiro aluno: ')
aluno4 = input('Digite o quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
#random.shuffle(lista)
shuffle(lista)
print('A ordem de apresentaçao dos alunos é: ')
print(lista)
