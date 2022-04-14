#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados:
#Foi usado cálculo de divisao inteira e depois divisao para se encontrar as casad decimais.

numero = int(input('Digite um número entre 0 e 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Seu número é {}, assim .. \nSua unidade é {}\nSua dezena é {}\nSua centena é {}\nSeu milhar é {}'.format(numero, unidade, dezena, centena, milhar))
