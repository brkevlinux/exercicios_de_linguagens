# Exercicio de Python V.3.
# Exercicio numero 38.

p = int(input('Digite o primeiro valor:'))
s = int(input('Digite o segundo valor: '))
if p < s:
	print(f'O primeiro valor {p} é menor que {s}.')
elif p > s:
	print(f'O segundo valor {s} é maior que {p}.')
else:
	print(f'Os dois valores sao iguais a {p}.')