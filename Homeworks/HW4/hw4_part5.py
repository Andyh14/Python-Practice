"""
File:         hw4_part5.py
Author:       Andy Huang
Date:         9/30/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program asks the user to guess the random integer.
It will give hints on whether the guess is too high or too low.
"""

import sys
from random import randint, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])

if __name__ == "__main__":
    number_answer = randint(1, 100)

    number_guess = int(input('Guess a number between 1 and 100: '))
    step_counter = 0

    while number_answer != number_guess:

        # checks if the guess is greater or less than the random int
        if number_guess < number_answer:
            print('Your guess is too low... Try something bigger!')
        if number_guess > number_answer:
            print('Your guess is to high... Try something smaller!')

        # increases the step counter so it can be printed out in the answer.
        step_counter += 1

        number_guess = int(input('Guess a number between 1 and 100: '))

    print('You guessed the value! It took you {} tries.'.format(step_counter))
























