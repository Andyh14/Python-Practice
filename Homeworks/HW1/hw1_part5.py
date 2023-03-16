"""
File:         hw1_part5.py
Author:       Andy Huang
Date:         9/9/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program calculates the energy contained in an object using the
Lorentz/Einstein equation. Only when given the rest mass and velocity.

"""
speed_of_light = int(299792458)

rest_mass = float(input("Enter the rest mass in kg: "))

velocity = float(input("Enter the velocity in m/s: "))

lorentz_energy = (rest_mass * (speed_of_light ** 2)) / ((1 - (velocity ** 2 / speed_of_light ** 2)) ** 0.5)

print('The Lorentz Energy in the object of rest mass {} and velocity {} is {}'.format(rest_mass,
                                                                                      velocity, lorentz_energy))







