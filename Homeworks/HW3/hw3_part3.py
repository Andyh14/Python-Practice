"""
File:         hw3_part3.py
Author:       Andy Huang
Date:         9/23/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This code adds or removes names from a list by using the command
"add" and "remove". It can also find the longest name in the list by
entering the command "max".

"""
if __name__ == "__main__":
    step_num = int(input('How many steps should we run? '))

    command_list = []
    name_list = []

    for i in range(step_num):
        command = str(input('Enter command: '))

        # adds just the name into name_list
        if 'add' in command:
            if 'add' in command:
                command_strip = command.lstrip('ad . / ')
                command_list.append(command_strip)
                print(command_strip, 'added.')

        # removes the name in name_list using .remove
        if 'remove' in command:
            command_strip = command.lstrip('remove ')

            if command_strip in command_list:
                command_list.remove(command_strip)
                print(command_strip, 'has been removed')
            else:
                print('That name has not been added to the list. ')

        if 'max' in command:
            short_word = long_word = command_list[0]

            # series of checks to find the long word.
            for x in range(0, len(command_list)):

                if len(short_word) < len(command_list[x]):
                    long_word = command_list[x]

                if len(long_word) > len(command_list[x]):
                    long_word = long_word

                if len(long_word) == len(command_list[x]):
                    first_word = long_word
                    second_word = command_list[x]
                    if first_word[0] < second_word[0]:
                        long_word = second_word
                    if first_word[0] > second_word[0]:
                        long_word = first_word

            print('The max name is', long_word)






















