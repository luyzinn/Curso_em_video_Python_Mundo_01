from datetime import datetime

print(datetime.today().strftime('%d/%m/%Y'))
print()


abertura = "Bem vindo a uma breve pesquisa!"

print(abertura)
print()
nome = input ('Qual o seu nome? ')
print('Olá {}!'.format(nome))
idade= int(input("Qual a sua idade? "))
celular = input("Você possui celular? ")
sistema = str(input("Qual o sistema operacional dele? "))

print("O sistema operacional do seu celular é {}" .format(sistema))
 
print("Obrigado pela sua participação!")



