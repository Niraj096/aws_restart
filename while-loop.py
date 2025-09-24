# while-loop.py
# Guess the Number game using a while loop

import random   # import random library

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Track whether the guess is correct
isGuessRight = False

# While loop keeps asking until guess is correct
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
