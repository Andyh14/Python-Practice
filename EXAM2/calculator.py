"""
File:         calculator.py
Author:       Andy Huang
Date:         11/21/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program will take in commands from a different file
and calculate the values in the file.
"""
COMMAND_CREATE = "create"
COMMAND_ADD = "add"
COMMAND_DISPLAY = "display"
COMMAND_MULTIPLY = "mul"


class Calculator:
    def __init__(self):
        self.dictionary_variables = {}

    def calculate(self, file_name):
        """
        This functio will take in a file loop through it looking for commands then execute the command.
        :param file_name: The name of the file with the information.
        :return
        """
        file_contents_list = []

        # loads the contents of the file into a list so that it can be looped through.
        with open(file_name, "r") as the_file:
            for line in the_file:
                file_contents_list.append(line)

        # loops through the list of information looking for commands.
        for string in range(len(file_contents_list)):
            split_string = file_contents_list[string].split()
            for index in range(len(split_string)):

                # finds the create command and executes the create function.
                if split_string[index] == COMMAND_CREATE:
                    self.create_variables(split_string[index + 1], split_string[index + 2])

                # finds the add command and executes the add function.
                elif split_string[index] == COMMAND_ADD:
                    self.add_variables(split_string[index + 1], split_string[index + 2], split_string[index + 3])

                # finds the multiply command and executes the multiply function.
                elif split_string[index] == COMMAND_MULTIPLY:
                    self.multiply_variables(split_string[index + 1], split_string[index + 2], split_string[index + 3])

                # finds the display command and executes the multiply function.
                elif split_string[index] == COMMAND_DISPLAY:
                    if split_string[index + 1] == "all":
                        self.display(None)
                    else:
                        self.display(split_string[index + 1])

    def display(self, variable_name):
        """
        This function will display the variable and it's value
        :param variable_name: The name of the specific variable you want to display
        :return:
        """
        # for specific variable information.
        if variable_name is not None:
            for key in self.dictionary_variables:
                if key == variable_name:
                    print(key, self.dictionary_variables[key])
        else:
            # all the information of every variable made.
            for key in self.dictionary_variables:
                print(key, self.dictionary_variables[key])

    def create_variables(self, variable_name, value):
        """
        This function will add the key that is the variable name and the value to the dictionary.
        :param variable_name: The name of the variable you want to create.
        :param value: The value you want to assign the variable
        :return
        """
        self.dictionary_variables[variable_name] = value

    def add_variables(self, var_or_value_one, var_or_value_two, variable):
        """
        This function will add two variables or values and assign it to a new variable or reassign to an old one.
        :param var_or_value_one: A variable or value to add
        :param var_or_value_two: A variable or value to add
        :param variable: The variable that is assigned the new value after adding.
        :return
        """
        # checks if the value is a variable or a value
        if var_or_value_one.isnumeric():
            value_one = var_or_value_one
        else:
            value_one = self.dictionary_variables[var_or_value_one]

        # same thing but for var_or_value two.
        if var_or_value_two.isnumeric():
            value_two = var_or_value_two
        else:
            value_two = self.dictionary_variables[var_or_value_two]

        self.dictionary_variables[variable] = int(value_one) + int(value_two)

    def multiply_variables(self, var_or_value_one, var_or_value_two, variable):
        """
            This function will multiply two variables or values and assign
            it to a new variable or reassign to an old one.
            :param var_or_value_one: A variable or value to multiply
            :param var_or_value_two: A variable or value to multiply
            :param variable: The variable that is assigned the new value after multiplying.
            :return
        """
        # checks if the value is a variable or a value
        if var_or_value_one.isnumeric():
            value_one = var_or_value_one
        else:
            value_one = self.dictionary_variables[var_or_value_one]

        # same thing but for var_or_value two.
        if var_or_value_two.isnumeric():
            value_two = var_or_value_two
        else:
            value_two = self.dictionary_variables[var_or_value_two]

        self.dictionary_variables[variable] = int(value_one) * int(value_two)


if __name__ == '__main__':
    file_name = input("What file do yo wish to run? ")
    calculator_object = Calculator()
    calculator_object.calculate(file_name)














