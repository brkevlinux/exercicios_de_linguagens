# Exercício 01 de Python com base no Curso em video.
# Exercícios resolvidos: 001; 002; 003 e 005.
nome = input('Qual o seu nome?\n')
print(f'Ola {nome}, bem-vindo ao terminal!')
valor_um = int(input('Digite um valor para calcular: '))
valor_dois = int(input('Digite mais um valor: '))
soma = valor_um + valor_dois
print(f''' O antecessor de {soma} e: {soma - 1},
 A soma de {valor_um} + {valor_dois} e de {soma},
 O sucessor de {soma} e: {soma + 1}.
	''')
