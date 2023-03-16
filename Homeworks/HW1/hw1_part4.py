"""
File:         hw1_part4.py
Author:       Andy Huang
Date:         9/9/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program calculates the commission amount given the car price.

"""

car_price = input('Enter the car price: ')
gross_profit = float(car_price) * 0.05
total_commission = float(gross_profit) * .25

print("You made {} dollar commission on that car sale!".format(total_commission))














