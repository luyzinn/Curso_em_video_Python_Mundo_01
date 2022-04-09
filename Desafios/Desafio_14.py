# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tempC = float(input('Qual a temperatura em graus Celsius? '))

tempF = (tempC * 1.8) + 32

print('A temperatura de {:.1f}C em Fahrenheit é igual a {:.1f}F'.format(tempC,tempF))