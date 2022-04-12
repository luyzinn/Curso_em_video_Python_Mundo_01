#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

'''from math import trunc

numero = float(input('Digite um número real: '))
print ('O valor digitado foi {}, e sua parte inteira é {}!'.format(numero, trunc(numero)))'''

num = float(input('Digite um número real: '))
print('O valor digitado foi {} e sua parte inteira é {}!!'.format(num, int(num)))