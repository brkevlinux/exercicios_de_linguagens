# Exercicio de Python v.3.
# Exercicio 008.

medida = float(input('digite a medida em metros: '))
print(f'''
|{medida / 1000:.5f}Km|
|{medida / 100:.4f}Hm|
|{medida / 10:.3f}Dam|
|{medida:.2f}M|
|{medida * 10:.2f}Dm|
|{medida * 100:.2f}Cm|
|{medida *1000:.2f}Mm|
	''')
