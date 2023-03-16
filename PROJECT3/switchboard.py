"""
File:    switchboard.py
Author:  Andy Huang
Date:    12/4/2020
Section: 46
E-mail:  andyh1@umbc.edu
Description:
    This program creates a switchboard class that is used in our network.py program.
"""

from phone import Phone


class Switchboard:
    def __init__(self, area_code):
        """
        :param area_code: the area code to which the switchboard will be associated.
        """
        # should be a integer
        self.area_code = area_code

        # list of local phone objects
        self.local_phones = []

        # dictionary of switchboard objects with keys being the area code
        self.local_switchboard = {}

        # list of local phone numbers
        self.local_phone_numbers = []

    def add_phone(self, phone_number):
        """
            This function adds a local phone connection by creating a phone object
            and storing it in this class.

        :param phone_number: integer phone number without area code
        :return: None
        """
        # checks for duplicate numbers in the same switch board. Even though
        # it shouldn't happen because of the network add phone function but the more checks the better.
        if phone_number not in self.local_phone_numbers:
            self.local_phone_numbers.append(phone_number)

            # creates phone object and appends to a list of phones associated with the switchboard.
            new_phone = Phone(phone_number, self)
            self.local_phones.append(new_phone)
        else:
            print("The number {} already exists.".format(phone_number))

    def add_trunk_connection(self, switchboard):
        """
            Connects the switchboard (self) to the switchboard (switchboard)

        :param switchboard: switchboard object to connect.
        :return: None
        """
        self.local_switchboard[switchboard.area_code] = switchboard

    def connect_call(self, area_code, number, previous_codes):
        """
        A recursive function that looks for a path to connect a call through different switchboards.

        :param area_code: the area code to which the destination phone belongs
        :param number: the phone number of the destination phone without area code.
        :param previous_codes: A empty list that keeps track of the previously tracked codes
        :return: True if a path can be found. None if not.
        """

        # base case for recursion
        if number in self.local_phone_numbers and self.area_code == area_code:
            return True

        # if statement checks to know when to stop searching for a path
        if len(previous_codes) != len(self.local_switchboard):
            if self.area_code not in previous_codes:
                previous_codes.append(area_code)
                for key in self.local_switchboard:

                    # recursive call for each switchboard that self is connected to.
                    if self.local_switchboard[key].connect_call(area_code, number, previous_codes):
                        return True

    def make_into_json_format(self):
        """
            This function will convert all the information in the switchboard
            into a json format for loading into a json file.

        :return: A dictionary that is in the correct format for a json file.
        """
        local_area_codes = []
        # turns the area codes in the trunk connected switchboards to a list of integer area codes.
        for area_code in self.local_switchboard:
            local_area_codes.append(area_code)

        return {self.area_code: {"Phones": self.local_phone_numbers, "Trunks": local_area_codes}}
