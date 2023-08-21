# Exercicios de Python3 V.3.
# Exercicio numero 16.

from math import trunc
num = float(input('Digite um numero: '))
print(f'''
	O valor digitado foi de: {num}.
	A sua porcao inteira e de {trunc(num)}
	Sem importar a biblioteca utilize o int(num){int(num)}.
''')