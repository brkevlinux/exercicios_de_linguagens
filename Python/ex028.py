# Exercicio de Python V.3,
# Exercicio numero 35.

print('-=' * 20)
print('Analizador de triangulos!')
print('-=' * 20)
lado_a = float(input('Digite o valor da primeira reta: '))
lado_b = float(input('Digite o valor da segunda reta: '))
lado_c = float(input('Digit o valor da terceira reta: '))
if lado_a < lado_b + lado_c and lado_b  < lado_a + lado_c and lado_c < lado_a + lado_b:
	print(f'As retas {lado_a}, {lado_b} e {lado_c} formam um triangulo!')
else:
	print(f'As retas {lado_a}, {lado_b} e {lado_c} nao formam um triangulo.')
