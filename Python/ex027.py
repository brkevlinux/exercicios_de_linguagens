# Exercicio de Python V.3.
# Exercicio numero 34.

sal = float(input('Qual é o seu salario atual? R$ '))
if sal <= 1250:
	print(f'O salario de {sal} passa a valer R${sal + (sal * (15 / 100)):.2f}')
else:
	print(f' O salario de {sal} passa a valer R${sal + (sal * (10 / 100)):.2f}')