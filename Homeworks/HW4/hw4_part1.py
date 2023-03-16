"""
File:         hw4_part1.py
Author:       Andy Huang
Date:         9/30/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  In this code you will play a game of rock, paper, scissors with the computer.

"""

import sys
from random import choice, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])

if __name__ == "__main__":

    play_game = input('Enter rock, paper, or scissors to play, stop to end. ')

    # while loop that keeps going till 'stop'
    while play_game != 'stop':
        the_choice = choice(['rock', 'paper', 'scissors'])

        if play_game == 'rock' or play_game == 'scissors' or play_game == 'paper':

            # all possible combinations and their outputs
            if play_game == 'rock' and the_choice == 'rock':
                print('Both rock, so it\'s a tie!')

            if play_game == 'rock' and the_choice == 'paper':
                print('Paper covers rock, you lose...')

            if play_game == 'rock' and the_choice == 'scissors':
                print('Rock crushes scissors, you win!')

            if play_game == 'paper' and the_choice == 'rock':
                print('Paper covers rock, you win!')

            if play_game == 'paper' and the_choice == 'paper':
                print('Both paper, so it\'s a tie!')

            if play_game == 'paper' and the_choice == 'scissors':
                print('Scissors cut paper, you lose...')

            if play_game == 'scissors' and the_choice == 'rock':
                print('Rock crushes scissors, you lose.. :(')

            if play_game == 'scissors' and the_choice == 'paper':
                print('Scissors cut paper, you win!')

            if play_game == 'scissors' and the_choice == 'scissors':
                print('Both scissors, so it\'s a tie!')
        else:
            print('You need to select rock, paper, or scissors...')

        play_game = input('Enter rock, paper, or scissors to play, stop to end. ')


