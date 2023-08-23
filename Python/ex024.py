# Exercicio de Python V.3.
# Exercicio numero 31.

dist = float(input('Digite a distancia percorrida: '))
# preco = dist > 200 if dist * 0.45 else dist * 0.50 
if dist > 200:
	print(f'A distancia percorrida foi de {dist:.2f}Km com valor de R${dist * 0.45:.2f}')
else:
	print(f'A distancia de {dist:.2f}Km  custa o valor de R${dist * 0.50:.2f}')