# Exercicio de Python V.3.
# Exercicio numero 011.

altura = float(input('Qual a altura da parede: '))
largura = float(input('Qual a largura da parede: '))
print(f'''
	A parede tem {altura}X{largura}m.
	com a sua area de {altura * largura:.2f}m².
	A quantidade de tinta será de {(altura * largura) / 2:.2f}l.
''')