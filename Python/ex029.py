# Exercicio de Python V.3.
# Exercicio numero 36.

sal = float(input('Qual e o salario: R$ '))
casa = float(input('Qual e o valor da casa: R$ '))
ano = int(input('Qual e o prazo de pagamento? '))
prestacao = casa / (ano * 12)
minimo = sal * 30 / 100
print(f'''
	Para pagar uma casa de R${casa:.2f} em {ano} anos,
	a prestação sera de R${prestacao:.2f}
	''')
if prestacao >= minimo:
	print(f'A prestacao exedeu o seu valor e o pedido foi negado')
else:
	print('O emprestimo sera concedido!')