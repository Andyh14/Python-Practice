"""
File:         hw3_part2.py
Author:       Andy Huang
Date:         9/23/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program calculates the Faulhaber Sum given the number of terms and the power value.

"""
if __name__ == "__main__":
    power_number = int(input('What is the power we want to use? '))

    term_number = int(input('How many terms do we want to calculate? '))

    if power_number > 0 and term_number > 0:
        list_terms = []

        # puts the range in list_terms
        for i in range(1, term_number + 1):
            list_terms.append(i)

        the_sum = 0
        # squares each term in list_terms and adds each new squared element together.
        for x in list_terms:
            x **= power_number
            the_sum += x
        print(the_sum)
    else:
        print('Both n and p must be non-negative')


























