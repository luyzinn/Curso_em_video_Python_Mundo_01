#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

from posixpath import split


nome = str(input('Escreva seu nome completo: ')).strip().split()
primero_nome = nome[0]
segundo_nome = nome[-1] #usando o -1 no módulo, sempre indicaremos a última posiçao dentro da sentença da variárel STR
print('Seu primeiro nome é {}\nSeu ultimo nome é {}!'.format(primero_nome, segundo_nome))
