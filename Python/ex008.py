# Exercicio de Python V.3.
# Exercicio numero 12.

preco = float(input('Qual é o preço do produto? R$ '))
desc = int(input('Qual é o desconto da loja? R$ '))
print(f'''
O produto custava R${preco:.2f},
na promoção com desconto de {desc}%,
o seu valor vai custar R${preco - (preco * (desc / 100)):.2f}
''')