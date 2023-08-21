# Exercicio de Python V.3.
# Exercicio numero 19.

from random import choice
a = str(input('Digite o nome do(a) primeiro(a) aluno(a): '))
b = str(input('Digite o nome do(a) segundo(a) aluno(a): '))
c = str(input('Digite o nome do(a) terceiro(a) aluno(a): '))
d = str(input('Digite o nome do(a) quarto(a) aluno(a): '))
lista = [a, b, c, d]
print(f'O(a) aluno(a) sorteado(a) foi: {choice(lista)}')