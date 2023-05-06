# Exercicio 02 de Python.
# Exercicio resolvido ex004.
entrada = input('Digite algo: ')
print(f'''
	O tipo primitivo dessa variavel e: {type(entrada)}
	A variavel esta somente com espacos? 
	{entrada.isspace()}
	A variavel possui valor somente numerico?
	{entrada.isnumeric()}
	A variavel possui somente valor alfabetico?
	{entrada.isalpha()}
	A variavel e alfa numerica?
	{entrada.isalnum()}

	''')