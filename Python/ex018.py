# Exercicio de Python V.3.
# Exercicio numero 24.

nome = str(input('Digite a cidade em que nasceu: \n'))
primerio = nome.split()
cid = primerio[0].lower() == 'santo'
print(f'''
	Analizando o nome: {nome}
	Voce nasceu na cidade: {cid}

	''')