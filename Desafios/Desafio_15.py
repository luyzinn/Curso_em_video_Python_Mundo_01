# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado:

dias = int(input('Quantos dias você ficou com o veículo? '))
km = float(input('Quantos Km você rodou com o veículo? '))
vdias = 60 #valor em reais por dia
vkm = 0.15 #valor por Km rodado
preco = float(dias * vdias) + (km * vkm)
print('Você ficou com o veículo {} dias, rodou {}Km!\nIsso gerou um custo total de R$ {:.2f}'.format(dias, km, preco))
