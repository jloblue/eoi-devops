import dice
from time import sleep


def roll(amount:int, sides:int):
    return dice.roll(f'{amount}d{sides}')

for idx, result in enumerate(roll(5,6)):
    print(f'Este es el Lanzamiento Nº {idx+1} Has tenido suerte !! el número obtenido {result}')
    sleep(5)
