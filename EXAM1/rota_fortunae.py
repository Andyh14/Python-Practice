"""
File:         rota_fortunae.py
Author:       Andy Huang
Date:         10/6/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program plays a game of hangman. It turns a users input into a series of blanks where the
user can guess the inputted word, letter by letter or the whole word/phrase.
"""
if __name__ == '__main__':
    input_string = input('What is the word you want the players to guess? ')
    string_list = list(input_string)

    # created lower case version of the string so lower case guesses can find upper case letters in the string.
    lowercase_input_string = input_string.lower()
    lower_case_string_list = list(lowercase_input_string)

    # created upper case version of the string so upper case guesses can find upper case letters in the string.
    uppercase_input_string = input_string.upper()
    upper_case_string_list = list(uppercase_input_string)

    guess_list = []

    # this loop creates the first blank string based on the length of the input.
    for letter in range(len(string_list)):
        if ord(string_list[letter]) == 32:
            guess_list.append(' ')
        else:
            guess_list.append('_')
    print(''.join(guess_list))

    list_of_guesses = []

    # creates & prints a new guess list if the guess is in the input string. If not it will print '_' in that index.
    # implements the 'solve' function where the user can input 'solve' to guess the full string.
    while guess_list != string_list:
        user_guess = input('Guess a letter, or "solve": ')

        # checks if the guess is a repeated guess
        if user_guess in list_of_guesses:
            print('You already guessed that! Try a different letter. ')

        list_of_guesses.append(user_guess)
        modifying_list = []

        if user_guess != "solve":

            # checks if the letter upper or lower case is in the list of guesses
            if user_guess in lower_case_string_list or user_guess in upper_case_string_list:

                # this loop checks if each letter in the input_string is in the guess_list
                for letter in range(len(string_list)):

                    # appends the letter if it is the guess_list
                    if lower_case_string_list[letter] in list_of_guesses or upper_case_string_list[letter] in list_of_guesses:
                        modifying_list.append(string_list[letter])

                    else:
                        # creates spaces and un-guessed letters
                        if ord(string_list[letter]) == 32:
                            modifying_list.append(' ')
                        else:
                            modifying_list.append('_')
            else:
                print('There are no {}\'s in the word/phrase. '.format(user_guess))

            guess_list = modifying_list
            print(''.join(guess_list))

        # solve function where you can cut in line and try to guess the whole string right off the bat.
        if user_guess == 'solve':
            user_string_guess = input('What is the entire puzzle? ')
            user_string_guess_list = list(user_string_guess)
            if user_string_guess_list == string_list or user_string_guess_list == lower_case_string_list:
                guess_list = string_list
            else:
                print('That wasn\'t the answer... Try guessing a few letters first.')

    print('You solved the puzzle!')
