"""
File:         find_diphthongs.py
Author:       Andy Huang
Date:         10/4/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program prints all the diphthong pairs in a given word and tells you how many there are
in a given word.
"""
if __name__ == "__main__":
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']

    string_input = input('enter a string with a lot of diphthongs: ')

    string_list = list(string_input)
    diphthong_counter = 0

    # start at one because the for loop starts at 0
    next_letter_index = 1

    for letter in string_list:

        # makes sure the index will not be out of range
        if next_letter_index <= len(string_list):

            # checks if the letter and the one after it is a vowel
            if letter in vowel_list and string_list[next_letter_index] in vowel_list:
                print(letter, string_list[next_letter_index], sep='')

                # remove only the first letter because the for loop will go on to the next letter in the list.
                # thus making it so the for loop doesn't check string_list[i] next it will check string_list[i + 1]
                string_list.remove(letter)
                diphthong_counter += 1

        # add one to get the next index in the list so we get pairs.
        next_letter_index += 1

    if diphthong_counter == 0:
        print('The diphthong count is 0')
    else:
        print('The diphthong count is', diphthong_counter)
