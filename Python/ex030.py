# Exercicio de Python V.3.
# Execiciio numero 37.

num = int(input('Digite um numero inteiro: '))
print('''Escolha uma base de conversao:
	[1] - converter para binario
	[2] - converter para octal
	[3] - converter hexadecimal
	''')
opcao = int(input('Digite a sua opcao: '))
if opcao == 1:
	print(f'O {num} convertido para binario é igual a {bin(num)}')
elif opcao == 2:
	print(f'O {num} convertido para octal é igual a {oct(num)}')
elif opcao == 3:
	print(f'O {num} convertido para hexadecimal é a {hex(num)}')
else:
	print('Valor invalido!')
