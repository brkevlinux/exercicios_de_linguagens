# Exercicio de Python V.3.
# Exercicio numero 23.

valor = int(input('Digite um numero: '))
n = str(valor)
print(f'''
	Analizando o numero {valor}:
	Unidade: {valor // 1 % 10}
	Dezena: {valor // 10 % 10}
	Centena: {valor // 100 % 10}
	Unid Milhar: {valor // 1000 % 10}
	''')
print(f'''
	Analizando o numero {valor} na forma de string:
	Unidade: 
	Dezenta: 
	Centena: 
	Unid Milhar:
	''')
