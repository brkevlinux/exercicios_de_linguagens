# Exercicio de Python V.3.
# Exercicio numero 13.

sal = float(input('Qual é o seu salario atual? R$ '))
ajuste = int(input('Qual é a porcentagem de ajuste? '))
print(f'''
O seu salario atual de R${sal:.2f},
com o aumento de {ajuste}% 
ira valer R${sal + (sal * ajuste / 100):.2f}
''')