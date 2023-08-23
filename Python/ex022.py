# Exercicio de Python V.3.
# Exercicio numero 29.

vel = int(input('Qual a velocidade do veiculo? \n'))
if vel >= 80:
	print(f'''Voce foi multado em R${(vel - 80) * 7:.2f}
Por andar acima da velocidade permitida.
		''')
print('Dirija com cuidado!')