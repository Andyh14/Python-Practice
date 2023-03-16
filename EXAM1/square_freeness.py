"""
File:         square_freeness.py
Author:       Andy Huang
Date:         10/4/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program determines if a given integer between 0 and 1000 inclusively is square-free. If
it is not square-free then the program will the tell the user what prime number squared can divide the given int.
"""
if __name__ == "__main__":
    number_input = int(input('Tell me a number x: '))

    square_free = True
    answer_list = []

    # check input so it is positive and not zero.
    if number_input >= 1:

        # checks even numbers and puts it through the equation to find the squared number.
        # if squared number is found make square free false so that I can print out what I want to.
        if number_input % 2 == 0:

            for number in range(2, int((number_input ** 0.5))):

                # divide by 2 only for even numbers
                divided_number_input = number_input / 2

                if divided_number_input % number == 0:
                    squared_number = number ** 2

                    if number_input % squared_number == 0:

                        # use append to a list because we only want the smallest number which will
                        # always be the first value appended to the list because of how range works.
                        answer_list.append(number)
                        square_free = False

        # checks even numbers and puts it through the equation to find the squared number.
        # if squared number is found make square free false so that I can print out what I want to.
        if number_input % 2 != 0:
            for number in range(2, int((number_input ** 0.5))):

                if number_input % number == 0:

                    divided_number_input = number_input / number

                    if divided_number_input % number == 0:
                        # use append to a list because we only want the smallest number which will
                        # always be the first value appended to the list because of how range works.
                        answer_list.append(number)
                        square_free = False

        # printing block that prints whether square free is true or false.
        if square_free:
            print(number_input, 'is square free')
        else:
            # uses the first index in the list to get the smallest number because the list will always be in increasing.
            print(number_input, 'is not square free {} squared divides it'.format(answer_list[0]))

    else:
        print('You cannot calculate the square freeness of', number_input)
