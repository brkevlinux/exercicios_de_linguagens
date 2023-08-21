# Exercicio de Python V.3.
# Execicio numero 17.

from math import hypot
cat_a = float(input('Comprimento do cateto adjacente: '))
cat_o = float(input('Comprimento do cateto oposto: '))
hipotenusa = hypot(cat_o, cat_a)
print(f'''
	O valor do cateto adjacente e de {cat_a:.2f}
	O valor do cateto oposto e de {cat_o:.2f}
	A hipotenusa do triangulo vale: {hipotenusa:.2f}
''')