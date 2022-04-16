#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

# from random import randint 
# Usar nesse caso a linha randint (0,5)
import random
from time import sleep #função do módulo time que faz o computador 'dormir' ou esperar um determinado tempo para prosseguir o algoritimo

print('=-='*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar..')
print('=-='*20)
numero = int(input('Em que número em pensei? '))
print('PROCESSANDO ...  ...')
sleep(2)
print('Perai .. deixa eu escolher aqui .. ')
sleep(2)
numero_pc = random.randrange(5)
if numero == numero_pc:
    print('ACERTOU! Eu realmente pensei no número {} Vocês esta de parabéns!'.format(numero_pc))
else:
    print('Eu escolhi o número {} .. VOCÊ ERROU .. EU GANHEI.. Que peninha..'.format(numero_pc))

