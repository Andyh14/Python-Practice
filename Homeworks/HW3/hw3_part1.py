"""
File:         hw3_part1.py
Author:       Andy Huang
Date:         9/23/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This code lists the tasks the user has and prints the tasks that are not finished yet.

"""
if __name__ == "__main__":
    num_tasks = int(input('How many tasks do you have? '))

    if num_tasks > 0:
        list_of_tasks = []
        to_do_list = []

        # Creates the range for the list of tasks and assigns the input into the list
        for i in range(0, num_tasks):
            task = input('What is your task? ')
            list_of_tasks.append(task)

        print('Here are your tasks: ')

        # Print the list in the format shown in example.
        for x in list_of_tasks:
            print(x)

        # Asks a question and puts the tasks in a different list only from the questions answered with "no"
        for y in list_of_tasks:
            question_answer = input('Have you completed "{}"?  (yes/no) '.format(y))
            if question_answer == 'no':
                to_do_list.append(y)

        # Prints the list that has the tasks that the user answered "no" to
        for word in to_do_list:
            print('A reaming task is {}'.format(word))

    else:
        print('That\'s either negative or zero')
























