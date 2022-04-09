n = float(input(' Digite um valor em metros: '))
cm = n * 100
mm = n * 1000
print('{} metros são iguais a {} cm.\nE é igual a {:.0f} mm.'.format(n, cm, mm))
# Para não usar casas decimais depois do ponto, mesmo em float usar: {:.0f}