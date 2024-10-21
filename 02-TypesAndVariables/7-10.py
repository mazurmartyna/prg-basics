import random

dice_roll = random.randint(1,6)

player = int(input('The computer has rolled the dice, your guess is: '))
result = player == dice_roll

print(f'Player has won: {result}')