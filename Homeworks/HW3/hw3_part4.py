"""
File:         hw3_part4.py
Author:       Andy Huang
Date:         9/23/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This code merges two lists of the same size. The size of the lists can
be modified.
"""
if __name__ == "__main__":

    list_one = []
    list_two = []
    list_combo = []

    number_elements = int(input('How many elements do you want to each list? '))

    # puts elements in list_one
    for element in range(number_elements):
        first_list_element = input('What do you want in the first list? ')
        list_one.append(first_list_element)

    # puts elements in list_two
    for element in range(number_elements):
        second_list_element = input('What do you want in the second list? ')
        list_two.append(second_list_element)

    # combines the two lists
    for element in range(number_elements):
        list_combo.append(list_one[element])
        list_combo.append(list_two[element])

    print('The first list is: {}'.format(list_one))
    print('The second list is: {}'. format(list_two))
    print('The merged list is: {}'.format(list_combo))






























