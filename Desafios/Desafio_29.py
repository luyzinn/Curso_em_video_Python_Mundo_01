# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade_atual = float(input('Qual a velocidade do veículo? Km/h ')) 
if velocidade_atual <= 80:
    print('Muito bem .. continue respeitando a velocidade máxima permitida que é de 80 Km/h!')
else:
    multa = (velocidade_atual - 80) * 7
    print('')
    print('Multado! Você excedeu o limite de velocidade que é de 80Km/h')
    print('Você deve pagar uma multa de R$ {:.2f} reais!'.format(multa))
print('')
print('Tenha um bom dia!')




