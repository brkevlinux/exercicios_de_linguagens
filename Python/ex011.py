# Exercicio de Python V.3.
# Exercicio numero 15.

dia = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos quilometros foram percorridos? '))
print(f'O aluguel do carro vai custar R${dia * 60 + km * 0.15:.2f}')