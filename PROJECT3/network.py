"""
File:    network.py
Author:  Andy Huang
Date:    12/4/2020
Section: 46
E-mail:  andyh1@umbc.edu
Description:
    This program sets up a network with switchboards and phones in a way
    that allow phones to connect with each other for conversation.
"""

# not used because I added more to switchboard function
from phone import Phone

from switchboard import Switchboard
import json

HYPHEN = "-"
QUIT = 'quit'
SWITCH_CONNECT = 'switch-connect'
SWITCH_ADD = 'switch-add'
PHONE_ADD = 'phone-add'
NETWORK_SAVE = 'network-save'
NETWORK_LOAD = 'network-load'
START_CALL = 'start-call'
END_CALL = 'end-call'
DISPLAY = 'display'


def start_connection(source_phone, destination_phone):
    """
        This function starts the connection by calling connect on a phone.

    :param source_phone: Phone object that wants to talk to another phone.
    :param destination_phone: Other phone object that the first phones wants to talk to.
    :return: Nothing
    """
    source_phone.connect(destination_phone)


class Network:
    def __init__(self):
        self.dictionary_switchboards = {}
        self.list_phones = []
        self.list_phone_numbers = []

    def load_network(self, filename):
        """
            This function clears all the information in the network
            then loads all the information from a json file.

        :param filename: the name of the file to be loaded.  Assume it exists and is in the right format.
                If not, it's ok if your program fails.
        :return:
        """
        # reset the networks specifications.
        self.dictionary_switchboards = {}
        self.list_phones = []
        self.list_phone_numbers = []

        with open(filename, 'r') as read_json:
            the_entire_file = read_json.read()
            the_entire_dictionary = json.loads(the_entire_file)

            # create switch boards with their keys
            for keys in the_entire_dictionary:
                area_code_integer = int(keys)
                new_switchboard = Switchboard(area_code_integer)
                self.dictionary_switchboards[area_code_integer] = new_switchboard

                # take that newly create switchboard and create the phones if there are any.
                if len(the_entire_dictionary[keys]["Phones"]) != 0:
                    for numbers in the_entire_dictionary[keys]["Phones"]:
                        self.add_phone(area_code_integer, numbers)

                # take that newly created switchboard and attempt to connect the trunk.
                if len(the_entire_dictionary[keys]["Trunks"]) != 0:
                    for code in the_entire_dictionary[keys]["Trunks"]:

                        # because the connect function is two ways we can say only
                        # connect when both switchboards exists
                        if code in self.dictionary_switchboards:
                            self.connect_switchboards(area_code_integer, code)

    def save_network(self, filename):
        """
            This function will save all the network information into a newly created json file.

        :param filename: the name of your file to save the network.  Remember that you need to save all the
            connections, but not the active phone calls (they can be forgotten between save and load).
            You must invent the format of the file, but if you wish you can use either json or csv libraries.
        :return:
        """
        # save all the possible phones whether a switchboard has it or not.
        switchboard_dict = {}
        for code in self.dictionary_switchboards:
            switchboard_dict.update(self.dictionary_switchboards[code].make_into_json_format())

        # saves it in a dictionary format.
        with open(filename, 'w') as game_file:
            game_file.write(json.dumps(switchboard_dict))

    def add_switchboard(self, area_code):
        """
        add switchboard creates a switchboard and add it to your network.

        By default it is not connected to any other boards and has no phone lines attached.
        :param area_code: A integer that is the area code for the new switchboard
        :return:
        """
        new_switchboard = Switchboard(area_code)
        self.dictionary_switchboards[area_code] = new_switchboard

    def connect_switchboards(self, area_1, area_2):
        """
            Connect switchboards connects the two switchboards (creates a trunk line between them)
            so that long distance calls can be made.

        :param area_1: The integer area-code of the first switchboard.
        :param area_2: The integer area-code of the second switchboard.
        :return:
        """
        first_switchboard = None
        second_switchboard = None

        # The function will connect both at the same time so you need both switchboards to exist.
        if area_1 in self.dictionary_switchboards and area_2 in self.dictionary_switchboards:

            # creates the first switchboard variable
            for board in self.dictionary_switchboards:
                if board == area_1:
                    first_switchboard = self.dictionary_switchboards[board]

            # creates the second switchboard variable
            for board in self.dictionary_switchboards:
                if board == area_2:
                    second_switchboard = self.dictionary_switchboards[board]

            # use the add trunk connection function on both switchboards.
            first_switchboard.add_trunk_connection(second_switchboard)
            second_switchboard.add_trunk_connection(first_switchboard)

        else:
            print("One of the switchboards doesn't exist ")

    def display(self):
        """
            Display outputs the status of the phone network as described in the project.
        """
        for board in self.dictionary_switchboards:
            object_switchboard = self.dictionary_switchboards[board]

            # prints first line specifying which switchboard is going to be displayed.
            print("Switchboard with area code:\t", object_switchboard.area_code)

            # trunk displays for the specified switchboard.
            print("\tTrunk lines are:")
            for key in object_switchboard.local_switchboard:
                print("\t\tTrunk line connected to: ", key)

            # phone displays for the specified switchboard.
            print("\tLocal phone numbers are:")
            for phone in object_switchboard.local_phones:

                # check for different displays. Depends on whether phone is connected or not.
                if phone.connected == False:
                    print("\t\tPhone with number: ", phone.number, "is not in use.")
                else:
                    print("\t\tPhone with number: ", phone.number, "is connected to", phone.connected_phone.full_number)
            print()

    def add_phone(self, area_code, phone_number):
        """
            Add phone finds the correct switchboard using the area code and
            adds the phone number to a list in network and calls the add phone
            function of the switchboard with the specified area code.

        :param area_code: The integer switchboard key to find the correct switchboard object.
        :param phone_number: The integer number to create a new phone object
        :return:
        """
        full_number = int(str(area_code) + str(phone_number))

        # if statements checks for repeated phone numbers.
        if full_number not in self.list_phone_numbers:
            for board in self.dictionary_switchboards:
                if self.dictionary_switchboards[board].area_code == area_code:
                    self.list_phone_numbers.append(full_number)
                    target_switchboard = self.dictionary_switchboards[board]
                    target_switchboard.add_phone(phone_number)
        else:
            print("That phone number already exists. ")

    def find_source_phone(self, source_area_code, source_phone_number):
        """
            This function will find the source phone object and return it.

        :param source_area_code: The switchboard key to find the correct switchboard object.
        :param source_phone_number: The phone number to find the correct phone object
        :return: The source phone object
        """
        for keys in self.dictionary_switchboards:
            if keys == source_area_code:
                for phone in self.dictionary_switchboards[keys].local_phones:
                    if phone.number == source_phone_number:
                        return phone

    def find_destination_phone(self, destination_area_code, destination_phone_number):
        """
             This function will find the destination phone object and return it.

        :param destination_area_code: The switchboard key to find the correct switchboard object.
        :param destination_phone_number: The phone number to find the correct phone object
        :return: The destination phone object
        """
        for keys in self.dictionary_switchboards:
            if keys == destination_area_code:
                for phone in self.dictionary_switchboards[keys].local_phones:
                    if phone.number == destination_phone_number:
                        return phone

    def disconnect_phone(self, area_code, number):
        """
            This function will call the disconnect function for
            the specific phone with the given credentials.

        :param area_code: A integer value that is the area code.
        :param number: A integer value that is the phone number.
        :return:
        """
        # Tries to find the phone.
        phone_object = self.find_source_phone(area_code, number)

        # if passes all these checks it will call the disconnect function.
        if phone_object != None:
            if phone_object.connected == True:
                print("Hanging up... ")
                phone_object.disconnect()
            else:
                print("Unable to disconnect. ")
        else:
            print("That phone does not exist. ")


if __name__ == '__main__':
    the_network = Network()
    s = input('Enter command: ')
    while s.strip().lower() != QUIT:
        split_command = s.split()
        if len(split_command) == 3 and split_command[0].lower() == SWITCH_CONNECT:
            area_1 = int(split_command[1])
            area_2 = int(split_command[2])
            the_network.connect_switchboards(area_1, area_2)
        elif len(split_command) == 2 and split_command[0].lower() == SWITCH_ADD:
            the_network.add_switchboard(int(split_command[1]))
        elif len(split_command) == 2 and split_command[0].lower() == PHONE_ADD:
            number_parts = split_command[1].split(HYPHEN)
            area_code = int(number_parts[0])
            phone_number = int(''.join(number_parts[1:]))

            # the code I added
            the_network.add_phone(area_code, phone_number)

        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_SAVE:
            the_network.save_network(split_command[1])
            print('Network saved to {}.'.format(split_command[1]))
        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_LOAD:
            the_network.load_network(split_command[1])
            print('Network loaded from {}.'.format(split_command[1]))
        elif len(split_command) == 3 and split_command[0].lower() == START_CALL:
            src_number_parts = split_command[1].split(HYPHEN)
            src_area_code = int(src_number_parts[0])
            src_number = int(''.join(src_number_parts[1:]))

            dest_number_parts = split_command[2].split(HYPHEN)
            dest_area_code = int(dest_number_parts[0])
            dest_number = int(''.join(dest_number_parts[1:]))

            # my code I added
            starting_phone = the_network.find_source_phone(src_area_code, src_number)
            ending_phone = the_network.find_destination_phone(dest_area_code, dest_number)

            # checks if both phones exists. If they do, then connect them.
            if starting_phone == None:
                print("The number {} does not exist.".format(src_number))
            elif ending_phone == None:
                print("The number {} does not exist.".format(dest_number))
            else:
                print("starting connection...")
                start_connection(starting_phone, ending_phone)

        elif len(split_command) == 2 and split_command[0].lower() == END_CALL:
            number_parts = split_command[1].split('-')
            area_code = int(number_parts[0])
            number = int(''.join(number_parts[1:]))

            # my code I added
            the_network.disconnect_phone(area_code, number)

        elif len(split_command) >= 1 and split_command[0].lower() == DISPLAY:
            the_network.display()

        s = input('Enter command: ')
