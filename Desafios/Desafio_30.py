# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número inteiro: '))
resultado = numero % 2 
if resultado == 0:
    print('')
    print('Seu número é par!')
else:
    print('')
    print('Seu número é ímpar!!')
