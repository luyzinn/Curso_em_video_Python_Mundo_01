#  Tipos primitivos

# Usado para saber qual o tipo primitivo: ,>> type() <<
# (Str - Stringer - Sempre se refere a palavras. Sempre usado entre aspas 'Olá', '7,5' )
# (Int - Se é número inteiro 7 , 8 , 10)
# (float - Se é número flutuante, que tem . separando, ou seja, se é um número real ex: 5.4)
# (Bool - Boleano - Ou True ou False - Quando se refere a valor lógico. Usar sempre Letra maiúscula)

print('== EXERCÍCIO 04 ==')
n = input('Digite algo: ')
print('1 - O tipo primitivo é: ',type(n)) 
print('2 - Tem somente espaços? ',n.isspace())
print('3 - É um número? ',n.isnumeric())
print('4 - É alfabetico? ',n.isalpha())
print('5 - É alfanumérico? ',n.isalnum()) 
print('6 - Esta em maiúculo? ',n.isupper()) #Usando para saber se esta todo em maiúsculo
print('7 - Esta em minúsculo? ',n.islower()) #Usado para saber se esta todo em minúsculo
print('8 - Esta capitalizado? ',n.istitle()) #Usado para saber se tem uma letra maiúscula





