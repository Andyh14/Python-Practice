"""
File:         hw1_part6.py
Author:       Andy Huang
Date:         9/9/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program calculates the gravitational force between two objects.
When given the objects mass and distance.

"""
g_constant = (6.674 * (1/(10 ** 11)))

mass_object1 = float(input("What is the mass of object 1, in kg? "))
mass_object2 = float(input('What is the mass of object 2, in kg? '))
distance = float(input('What is the distance in meters between the objects? '))
gravity_force = float((g_constant * mass_object1 * mass_object2) / (distance ** 2))

print('The gravitational force between the two objects is: {}'.format(gravity_force))








