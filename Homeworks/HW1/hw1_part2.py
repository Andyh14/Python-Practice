"""
File:         hw1_part2.py
Author:       Andy Huang
Date:         9/9/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program states what type a pokemon it is and what move it has learned.


"""

pokemon_name = input('What is the Pokemon\'s name? ')

pokemon_type = input('What is the Pokemon\'s type? ')

pokemon_move = input('What move would you like your Pokemon to learn? ')

print("Your {} type {}, has learned the move {}.".format(pokemon_type,
                                                         pokemon_name, pokemon_move))



