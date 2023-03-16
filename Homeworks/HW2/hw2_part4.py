"""
File:         hw2_part4.py
Author:       Andy Huang
Date:         9/15/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program will ask the user to input a year and output whether the year is a leap
year.

"""

leap_year_question = int(input('Which year do you want to know if it is a leap year? '))

if leap_year_question < 1:
    print('The year is less than 1 AD/CE, we aren\'t going back in time.')
else:
    if leap_year_question % 4 == 0:
        leap_year = True
        if leap_year_question % 100 == 0:
            leap_year = False
            if leap_year_question % 400 == 0:
                leap_year = True
        if leap_year:
            print('This is a leap year. ')
        else:
            print('This is not a leap year. ')
    else:
        print('This is not a leap year. ')






















