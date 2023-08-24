# Exercicio de Python V.3.
# Exercicio numero 40.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a ultima nota: '))
media = (n1 + n2 + n3 + n4) / 4
if media < 5:
	print('-=' * 25)
	print(f'''
| nota 1 | nota 2 | nota 3 | nota 4 | media |
|  {n1:.2f}  |  {n2:.2f}  | {n3:.2f}  |  {n4:.2f}  | {media:.2f}  |
		''')
	print('-=' * 25)
	print(' O aluno esta reprovado!')
elif media > 5:
	print('-=' * 25)
	print(f'''
| nota 1 | nota 2 | nota 3 | nota 4 | media |
|  {n1:.2f}  |  {n2:.2f}  | {n3:.2f}  |  {n4:.2f}  | {media:.2f}  |
		''')
	print('-=' * 25)
	print('O aluno esta aprovado!')
else:
	print('-=' * 25)
	print(f'''
| nota 1 | nota 2 | nota 3 | nota 4 | media |
|  {n1:.2f}  |  {n2:.2f}  | {n3:.2f}  |  {n4:.2f}  | {media:.2f}  |
		''')
	print('-=' * 25)
	print('O aluno esta aprovado com media minima.')