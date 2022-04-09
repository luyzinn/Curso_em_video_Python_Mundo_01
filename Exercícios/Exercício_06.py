print('== DESAFIO 06 ==')

n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)
#print('Analisando {}, percebe-se que: \no seu dobro é {},\nseu triplo é {}\ne a raiz é {:.2f}'.format(n, d, t, r))

print('Analisando {}, percebe-se que: \no seu dobro é {}, \nseu triplo é {} \ne a raiz é {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))))
# A raiz quadrada também pode ser feita com a função >>  pow(n, (1/2)) <<  pow significa power ou potência

