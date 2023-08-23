# Exercicio de Python V.3.
# Exercicio numero 32.

from datetime import date
print('Para analisar o ano atual digite 0.')
ano = int(input('Deseja analisar qual ano? '))
if ano == 0:
	ano = date.today().year
	if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
		print(f'O ano {ano} é BISSEXTO!')
	else:
		print(f'O ano {ano} NAO e BISSEXTO.')