# Exercicio de Python V.3.
# Exercicio numero 26.

frase = str(input('Digite uma frase: \n'))
verificar = frase.strip().lower()
print(f'''
	Analizando a frase temos:
	A letra A aparece na posição: {verificar.find('a') + 1} primeiro.
	A letra A aparece {verificar.count('a')} vezes.
	A ultima posicao em que a letra A aparece  e: {verificar.rfind('a') + 1}
	''')