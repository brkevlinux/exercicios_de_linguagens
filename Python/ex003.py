# Exercício 03 de Python.
#Exercícios 006

numero = int(input('Digite um numero inteiro: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print(f''' O numero digitado foi {numero};
	O dobro do numero é: {dobro};
	O triplo do numero e: {triplo};
	A sua raiz quadrada é: {raiz}
	''')
print(f'A média aritimetica é: {(numero + dobro + triplo + raiz) / 4}')