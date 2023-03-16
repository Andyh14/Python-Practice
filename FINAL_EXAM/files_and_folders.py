"""
File:    files_and_folders.py
Author:  Andy Huang
Date:    12/14/2020
Section: 46
E-mail:  andyh1@umbc.edu
Description:
    This program implements three classes, CommandLine, Directory, and File.
    The user can then navigate through CommandLine using commands.

"""


class CommandLine:
    def __init__(self):
        self.root = Directory("root", None)
        self.current_path = self.root

    def run(self):
        command = input('>>> ')
        while command.strip().lower() != 'exit':
            split_command = command.split()
            if len(split_command):
                if split_command[0] == 'ls':
                    self.current_path.display()
            if len(split_command) >= 2:
                if split_command[0] == 'cd':
                    self.change_directory(split_command[1])
                elif split_command[0] == 'makedir':
                    self.current_path.create_directory(split_command[1])
                elif split_command[0] == 'fcreate':
                    self.current_path.create_file(split_command[1])
                elif split_command[0] == 'fwrite':
                    self.current_path.file_write(split_command[1])
                elif split_command[0] == 'fread':
                    self.current_path.file_read(split_command[1])
                elif split_command[0] == 'fclose':
                    self.current_path.close_file(split_command[1])
                elif split_command[0] == 'fopen':
                    self.current_path.open_file(split_command[1])

            command = input('>>> ')

    def change_directory(self, dir_name):
        """
            This function will change the current path to a different directory.

        :param dir_name: THe name of the new directory.
        :return: None
        """

        # checks if the user is trying to access one level down.
        if dir_name in self.current_path.list_dir_names:
            for each in self.current_path.list_directory:
                if each.name == dir_name:

                    # changes the current path to one level down
                    self.current_path = each

        # checks if the user is trying to access one level up.
        elif dir_name == self.current_path.parent.name:

            # changes the current path to one level up.
            self.current_path = self.current_path.parent


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.list_all_names = []

        self.list_file_names = []
        self.list_dir_names = []

        # directory objects inside the directory
        self.list_directory = []

        # file objects inside the directory
        self.list_files = []

    def display(self):
        """
            This function will display all the names of the files and directories.

        :return: None
        """
        # the variable i will make sure it displays only five names per line.
        i = 0

        empty_line = ""
        print("ls for directory {}".format(self.name))
        for name in self.list_all_names:
            if i != 0 and i % 5 == 0:
                empty_line += "\n"
            empty_line += name + " "
            i += 1
        print(empty_line)

    def create_file(self, file_name):
        """
            This function will create a file and set its file state to False.

        :param file_name: The name of the newly created file.
        :return: None
        """

        # checks for duplicates and if not then create the file.
        if file_name not in self.list_file_names:
            new_file = File(file_name)
            new_file.file_state = False
            self.list_file_names.append(file_name)
            self.list_all_names.append(file_name)
            self.list_files.append(new_file)
        else:
            print("A file with that name already exists. ")

    def create_directory(self, dir_name):
        """
            This function will create a directory if the name doesn't already exist.

        :param dir_name: Name of the new directory to be made.
        :return: None
        """

        # same as create file except for directories.
        if dir_name not in self.list_dir_names:
            new_dir = Directory(dir_name, self)
            self.list_dir_names.append(dir_name)
            self.list_all_names.append(dir_name)
            self.list_directory.append(new_dir)
        else:
            print("A directory with that name already exists. ")

    def file_write(self, file_name):
        """
            This function will add contents to a file if the file is open.

        :param file_name: The file the user wants t write in.
        :return: None
        """
        # this block of code is for finding the correct file.
        target_file = None
        for each in self.list_files:
            if each.name == file_name:
                target_file = each

        # will only execute the write function if the file exists and is open.
        if target_file != None and target_file.file_state == True:
            file_contents = input("Enter file contents for {}: ".format(target_file.name))
            target_file.write(file_contents)

    def file_read(self, file_name):
        """
            This function will print the file contents.

        :param file_name: The name of the file that wants to be read.
        :return: None
        """
        # this block of code is for finding the correct file.
        target_file = None
        for file in self.list_files:
            if file.name == file_name:
                target_file = file

        # printing out the contents in the correct format.
        print("Contents of {}: ".format(file_name))
        print(target_file.contents)

    def close_file(self, file_name):
        """
            This function will close a specific file.

        :param file_name: A specific file to be closed.
        :return: None
        """
        # this block of code is for finding the correct file.
        target_file = None
        for file in self.list_files:
            if file.name == file_name:
                target_file = file

        # calling the close function.
        if target_file != None:
            target_file.close()

    def open_file(self, file_name):
        """
            This function will call a file's function to open itself.

        :param file_name: The name of the specific file to open
        :return: None
        """
        # this block of code is for finding the correct file.
        target_file = None
        for file in self.list_files:
            if file.name == file_name:
                target_file = file

        # calling the open function
        if target_file != None:
            target_file.open()


class File:
    def __init__(self, name):
        self.name = name
        self.file_state = None
        self.contents = ""

    def open(self):
        """
            This function will clear the file contents and open it.

        :return: None
        """
        self.file_state = True
        self.contents = ""

    def close(self):
        """
            This function will close the file by setting the file state to False.

        :return: None
        """
        self.file_state = False

    def write(self, input_text):
        """
            This function will add the user input into the contents of the file
            in the correct format.

        :param input_text: The user input to write in the file.
        :return: None
        """
        self.contents += input_text + "\n"


if __name__ == '__main__':
    cmd_line = CommandLine()
    cmd_line.run()
