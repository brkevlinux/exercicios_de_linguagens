# Exercicio de Python V.3.
# Criando um mini jogo!!

from random import randint
from time import sleep
jogador = int(input('Digite um numero natural de [0 a 9]: \n'))
pc = randint(0, 9) 
print('Processando...')
sleep(3)
if (jogador == pc):
	print(f'Parabens! Voce acertou o numero {pc}.')
else:
	print(f'Que pena! Voce perdeu. O numero sorteado foi {pc}.')