"""
File:         smart_house.py
Author:       Andy Huang
Date:         11/19/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This function can put devices in houses and store them in a file then load the information from a file.

"""
TRUE_CONSTANT = "True"
FALSE_CONSTANT = "False"
NAME_CONSTANT = "name:"
TOGGLE_CONSTANT = "toggle:"
WRONG_ADDY_CONSTANT = "That file does not correlate with the current address \n Do you want to continue and overwrite your currnet address? (yes/no)?"


class Device:
    def __init__(self, name, toggle):
        self.name = name
        self.toggle = toggle


class SmartHouse:
    def __init__(self, address):
        self.address = address
        self.devices = []

    def add_device(self, device):
        """
        This function will add a device into the house
        :param device: A class object with a name and a toggle.
        :return
        """
        # checks if the device is already in the house and if not then adds it to the list.
        if device not in self.devices:
            self.devices.append(device)
        else:
            print("That device is already in the house. ")

    def get_device(self, the_id):
        """
        This function will search for a specific device in the house class and return it.
        :param the_id: The name of the device to search for.
        :return: The found device.
        """
        # searches for the specific device and returns it.
        for device in self.devices:
            if device.name == the_id:
                return device

    def save_house(self, file_name):
        """
        This function creates a new file with the houses devices and their information.
        :param file_name: The name of the file to be created.
        :return
        """
        # opens the file and saves all the devices into it.
        with open(file_name, "w") as the_file:
            the_file.write(self.address + "\n")
            for device in self.devices:
                the_file.write("name: {} toggle: {}".format(device.name, device.toggle) + "\n")

    def load_house(self, file_name):
        """
        This function will reset the devices in the house and add the devices saved in the file that the user calls.
        :param file_name: The name of the file that the user wants to get information from.
        :return
        """
        # resets the devices in the house by clearing them.
        self.devices = []
        file_contents_list = []

        # opens the specific file and adds each line to a list.
        with open(file_name, "r") as the_file:
            for line in the_file:
                file_contents_list.append(line)

        # checks if the current address matches with the information being accessed in the file.
        if self.address != file_contents_list[0].rstrip():
            continue_input = input(WRONG_ADDY_CONSTANT)
            if continue_input == "yes":
                self.address = file_contents_list[0].rstrip()

        # function should only execute when the current address matches with the address of the chosen file.
        if self.address == file_contents_list[0].rstrip():

            # sets up local variables, then makes new devices with the information in the file.
            for string in range(1, len(file_contents_list)):
                new_device_name_list = []
                new_device_toggle = None
                split_string = file_contents_list[string].split()

                # loop through every word to find key words to then find the wanted information.
                for index in range(len(split_string)):
                    if split_string[index] == NAME_CONSTANT:
                        new_device_name_list.append(split_string[index + 1].rstrip())

                    # the case if the name of device is more than one word
                    elif split_string[index].rstrip() in new_device_name_list:
                        if split_string[index + 1] != TOGGLE_CONSTANT:
                            new_device_name_list.append(split_string[index + 1])

                    elif split_string[index] == TOGGLE_CONSTANT:
                        new_device_toggle = split_string[index + 1]

                # code added in the case of device names that are more than one word long.
                if len(new_device_name_list) == 1:
                    new_name = new_device_name_list[0]
                else:
                    new_name = " ".join(new_device_name_list)

                # make the toggle variable not equal a string
                if new_device_toggle == TRUE_CONSTANT:
                    new_device_toggle = True
                elif new_device_toggle == FALSE_CONSTANT:
                    new_device_toggle = False

                # creates new device with new information in the file and appends them to the list.
                device = Device(new_name, new_device_toggle)
                self.devices.append(device)

    def display(self):
        """
        This function displays the devices and their information.
        :return
        """
        print("For the house at {}: ".format(self.address))
        for device in self.devices:
            if device.toggle:
                print("\t {} is on".format(device.name))
            elif device.toggle == False:
                print("\t {} is off".format(device.name))


if __name__ == '__main__':
    address = input('What is the address of the house?')
    house = SmartHouse(address)

    command = input('What do you want to do? (add device, toggle device, load <file>, save <file>, display) ').lower()
    while command != 'quit':
        if command == 'add' or command == 'add device':
            the_id = input('What is the device id?')
            if not house.get_device(the_id):
                yes_no = input('Is the device on? (yes/no)')
                if yes_no == 'yes':
                    house.add_device(Device(the_id, True))
                elif yes_no == 'no':
                    house.add_device(Device(the_id, False))
            else:
                print('There is no device id: {} in the ')
        elif command == 'toggle' or command == 'toggle device':
            the_id = input('What is the device id?')
            the_device = house.get_device(the_id)
            if the_device:
                on_off_toggle = input('On, Off or Toggle? ').lower()
                if on_off_toggle == 'on':
                    the_device.toggle = True
                elif on_off_toggle == 'off':
                    the_device.toggle = False
                elif on_off_toggle == 'toggle':
                    the_device.toggle = not the_device.toggle
            else:
                print('There is no device id: {} in the ')
        elif command == 'load':
            file_name = input('What is the filename to load from? ')
            house.load_house(file_name)
            print('The house has been loaded from {}'.format(file_name))
        elif command == 'save':
            file_name = input('What is the filename to save as? ')
            house.save_house(file_name)
            print('The house has been saved in {}'.format(file_name))
        elif command == 'display':
            house.display()
        else:
            print('unknown command', command)

        command = input(
            'What do you want to do? (add device, toggle device, load <file>, save <file>, display) ').lower()
