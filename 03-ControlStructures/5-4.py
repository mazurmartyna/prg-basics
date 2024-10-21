# A simple number guessing game

import random

# Randomly chosen number to be guessed from 1 to 100
number_to_guess = random.randint(1, 100)
user_guess = 0

print("Guess the number between 1 and 100!\n")

while user_guess != number_to_guess:
    user_guess = int(input('Enter your guess: '))
    if user_guess < number_to_guess:
        print('Too low! Try again.\n')
    elif user_guess > number_to_guess:
        print('Too high! Try again.\n')
    else:
        print('Congratulations! You guessed the correct number!')