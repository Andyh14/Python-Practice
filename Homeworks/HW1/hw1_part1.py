"""
File:         hw1_part1.py
Author:       Andy Huang
Date:         9/9/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program states how many cats, dogs, or fish the programmer has and
the total, his favorite restaurant, and the golden ratio.

"""

favorite_restaurant = "Popeyes"
num_dogs = 4
num_cats = 5
num_fish = 25
golden_ratio = 1.618

print("My favorite restaurant is " + favorite_restaurant)

print("The golden ratio is {}".format(golden_ratio))

print("I have {} dogs, {} cats, and {} fish".format(num_dogs, num_cats, num_fish))

print("And so I have a total of {} pets".format(num_cats + num_fish + num_dogs))
