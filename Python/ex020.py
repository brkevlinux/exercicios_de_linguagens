# Exercicio de Python3 V.3.
# Exercicio numero 27.

nome = str(input('Digite o seu nome: ')).strip()
lista = nome.split()
contador = len(lista)
print(f'''
	Muito Prazer em te conhecer!
	Seu primeiro nome é: {lista[0]}
	Seu ultimo nome é: {lista[contador - 1]}
	''')

# Outra forma de apresentação.
print(f'''
	{lista[len(lista) - 1]}, {lista[0]}
	Muito prazer em te conhecer!
	''')