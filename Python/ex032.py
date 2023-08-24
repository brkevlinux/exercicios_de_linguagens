# Exercicio de Python V.3.
# Exercicio numero 39.

from datetime import date
nasc = int(input('Digite o seu ano de nacimento: '))
ano = date.today().year
if ano - nasc < 18 and ano - nasc > 14:
	print(f'''
		A sua idade e de {ano - nasc}.
Sua classificacao esportiva e Junior
		''')
elif ano - nasc > 18:
	print(f'''A sua idade e de {ano - nasc}
		Pode fazer a selecao para competicao proficional.
		''')
else:
	print(f'''
		A sua idade e de {ano - nasc}.
		A sua classificacao esportiva e Infantil.
		''')