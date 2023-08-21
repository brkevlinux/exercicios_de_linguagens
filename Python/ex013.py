# Exercicio de Python V.3.
# Execicio numero 17, 18.

from math import hypot, sin, cos, tan, radians
cat_a = float(input('Comprimento do cateto adjacente: '))
cat_o = float(input('Comprimento do cateto oposto: '))
hipotenusa = hypot(cat_o, cat_a)
print(f'''
	O valor do cateto adjacente e de {cat_a:.2f}
	O valor do cateto oposto e de {cat_o:.2f}
	A hipotenusa do triangulo vale: {hipotenusa:.2f}
''')

angulo = float(input('Digite um angulo: '))
print(f'''
	Para o angulo de {angulo:.2f}º temos:
	O seno de {sin(radians(angulo)):.2f}
	O cosseno de {cos(radians(angulo)):.2f}
	E a tangente de {tan(radians(angulo)):.2f}
	''')