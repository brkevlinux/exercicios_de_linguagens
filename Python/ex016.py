# Exercicio de Python V.3.
# Exercicios numero 22 e 25.

nome = str(input('Digite o seu nome: '))
primeiro = nome.split()
print(f'''
	Seu primeiro nome e {primeiro[0]} e possui {len(primeiro[0])}
	Seu nome ao todo tem {len(nome.strip()) - nome.count(' ')} letras.
	Seu nome em minusculas {nome.lower()}
	Seu nome em maiusculas {nome.upper()}
	O seu nome possui Silva? {'silva' in nome.lower()}
	''') 