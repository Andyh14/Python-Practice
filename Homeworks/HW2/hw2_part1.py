"""
File:         hw2_part1.py
Author:       Andy Huang
Date:         9/14/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description: This program calculates whether the user has enough ingredients to bake zucchini bread. If the user
does not have enough of any ingredient then the program will point out which ingredient is lacking.


"""

print("Welcome to the \"Can we make zucchini bread today?\" calculator! ")

brown_sugar = float(input("How many cups of brown sugar do you have? "))

white_sugar = float(input("How many cups of white sugar do you have? "))

num_eggs = int(input("How many eggs do you have? "))

vegetable_oil = float(input('How many cups of vegetable oil do you have? '))

cups_flour = float(input('How many cups of flour do you have? '))

giant_zucchini = input("Do you have a giant zucchini? ")

if brown_sugar < 1:
    print('You do not have enough brown sugar!')
if white_sugar < 1:
    print('You do not have enough white sugar!')
if num_eggs < 2:
    print('You do not have enough eggs!')
if vegetable_oil < 1:
    print('You do not have enough vegetable oil!')
if cups_flour < 3:
    print('You do not have enough flour!')
if giant_zucchini.lower() == "no":
    print('You need to get a giant zucchini!')
else:
    print('You are good to go! Let\'s get baking!')















