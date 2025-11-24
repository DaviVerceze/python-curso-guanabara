#Jogo da adivinhação

import random

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
numero = int(input('Em que número eu pensei: '))

n = random.randint(0, 5)

if numero == n:
    print('Parabéns! Você ganhou.')
else:
    print(f'Você errou! o número em que pensei foi {n}')