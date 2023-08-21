# Exercicio de Python V.3.
# Execicio numero 20.

import random
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'''
	A ordem de nomes do grupo para apresentar e:
	{lista}
''')