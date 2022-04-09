#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros:

v = float(input("Digite o valor em metros: "))
c = v / 100
m = v / 1000
print("{}m corresponde a {}cm e {}mm".format(v,c,m))
