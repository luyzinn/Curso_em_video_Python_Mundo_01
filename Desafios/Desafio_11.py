#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2m²:

l = float(input("Digite a largura da parede em metros: "))
alt = float(input("Digite a altura da parede em metros: "))
area = l * alt
t = area / 2
print("A área da sua parede é de {:.2f}m², sabendo que cada litro de tinta rende 2m², \n voce precisará de {:.2f} litros de tinta".format(area,t))