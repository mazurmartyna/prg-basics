import random

dice_roll1 = random.randint(1,6)
dice_roll2 = random.randint(1,6)
dice_roll3 = random.randint(1,6)

total = dice_roll1 + dice_roll2 + dice_roll3

print(f'The sum of 3 dice rolls {dice_roll1}, {dice_roll2} and {dice_roll3} is {total}')