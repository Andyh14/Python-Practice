"""
File:    phone.py
Author:  Andy Huang
Date:    12/4/2020
Section: 46
E-mail:  andyh1@umbc.edu
Description:
    This program defines the basic functionality that you need from a phone.
    The phone class is used by the network.py program and switchboard.py program.
"""
HYPHEN = "-"


class Phone:
    def __init__(self, number, switchboard):
        """
        :param number: A integer phone number without area code
        :param switchboard: The object switchboard to which the number is attached.
        """
        self.number = number
        self.switchboard = switchboard
        self.full_number = str(self.switchboard.area_code) + HYPHEN + str(self.number)
        self.connected = False
        self.connected_phone = None

    def connect(self, other_phone):
        """
        This function will take another phone to connect to and connect this phone and the other one.
        :param other_phone: the other phone object to connect to.
        :return: None
        """
        # calls the recursive connect call function from the switchboard the phone is connected to.
        connected_factor = self.switchboard.connect_call(other_phone.switchboard.area_code, other_phone.number, [])

        # if path can be found and the other phone is not connected already then it will change the connected factor.
        if connected_factor == True:
            if not other_phone.connected:

                # makes the connection factor true for both phones
                other_phone.connected = True
                self.connected = True

                # makes it so we know what phone is connected to which phone for both phones.
                other_phone.connected_phone = self
                self.connected_phone = other_phone
                print("{} and {} are now connected.".format(self.full_number, other_phone.full_number))
            else:
                print(other_phone.number, "is already connected to a phone at the moment")
        else:
            print("{} and {} could not be connected.".format(self.full_number, other_phone.full_number))

    def disconnect(self):
        """
            This function should disconnect two phones and show the connection status to disconnected.
        :return: None
        """

        # changes connected factor to normal
        self.connected = False
        self.connected_phone.connected = False
        phone_number_connected = self.connected_phone.number

        # takes off the connected phone object
        self.connected_phone.connected_phone = None
        self.connected_phone = None

        print(phone_number_connected, "has been disconnected to", self.number)
