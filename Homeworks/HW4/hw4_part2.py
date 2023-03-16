"""
File:         hw4_part2.py
Author:       Andy Huang
Date:         9/30/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This code translates your string into a coded language by going through the Caesar Salad Cipher.

"""
if __name__ == "__main__":
    input_string = input('What is the string to encrypt? (or stop) ')

    while input_string != 'stop':
        key = int(input('what is the offset? '))
        final_word = ''

        for index in range(len(input_string)):

            # takes each letter in the string to be used in the if statements.
            input_char = input_string[index]

            # checks for upper case letters then add the new letter to the string after algorithm.
            if 65 <= ord(input_char) <= 90:

                alphabet_char_upper = ord(input_char) - 65

                new_alphabet_num = (alphabet_char_upper + index ** 2 + key) % 26

                final_char = chr(new_alphabet_num + 65)

                final_word = final_word + final_char

            # checks for lower case letters then add the new letter to the string after algorithm.
            if 97 <= ord(input_char) <= 122:
                alphabet_char_lower = ord(input_char) - 97

                new_alphabet_num = (alphabet_char_lower + index**2 + key) % 26

                final_char = chr(new_alphabet_num + 97)

                final_word = final_word + final_char

            # checks if is a space then add space to the string
            if ord(input_char) == 32:
                final_word = final_word + chr(32)

        print('The encrypted string is:', final_word)

        input_string = input('What is the string to encrypt? (or stop) ')












































