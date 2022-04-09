#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p = float(input("Digite o valor do produto: R$ "))
liq = p -(p * 0.05)
print("Estamos em liquidaçao!! E o valor do produto com 5% de desconto é de: R$ {:.2f}".format(liq))