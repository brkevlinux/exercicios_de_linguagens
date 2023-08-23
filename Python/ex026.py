# Exercicio de Python V.3.
# Exercicio numero 33.

p = int(input('Digite o primeiro valor:'))
s = int(input('Digite o segundo valor: '))
t = int(input('Digite o terceiro valor: '))
menor = p
maior = p
if s < p and s < t:
	menor = s
if t < p and t < s:
	menor = t
if  s > p and s > t:
	maior = s
if t > p and t > s:
	maior = t
print(f'''
	O menor valor é o {menor},
	O maior valor é o {maior}.
	''')