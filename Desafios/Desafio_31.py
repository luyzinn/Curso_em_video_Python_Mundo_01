# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

from time import sleep

distancia_percorrida = float(input('Qual a distância da sua viagem em KM? '))
passagem_1 = distancia_percorrida * 0.50
passagem_2 = distancia_percorrida * 0.45
if distancia_percorrida < 200:
    print('')
    print('A distância é de {} Km, inferior a 200 Km. Nesse caso o valor por KM é de R$ 0.50. Sendo assim:'.format(distancia_percorrida))
    '''print('.')
    sleep(2)
    print('.')
    sleep(2)
    print('.')
    sleep(2)'''
    print('O valor da passagem é R$ {:.2f}'.format(passagem_1))
else:
    print('')
    print('A distância é de {} Km, superior a 200 Km. Nesse caso o valor por KM é de R$ 0.45. Sendo assim:'.format(distancia_percorrida))
    '''print('.')
    sleep(2)
    print('.')
    sleep(2)
    print('.')
    sleep(2)'''
    print('O valor da passagem é R$ {:.2f}'.format(passagem_2))