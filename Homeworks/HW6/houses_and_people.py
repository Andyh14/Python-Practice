"""
File:         houses_and_people.py
Author:       Andy Huang
Date:         11/03/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This programs lets you create people and houses and
put people in houses and also take them out.
"""


class Person:
    def __init__(self, name):
        self.name = name
        self.the_house = None

    # gives the name to put into the house list in the house object
    def go_in(self, house):
        self.the_house = house
        house.in_house(self.name)

    # gives the name to take out of the list in the house object
    def leave(self, house):
        self.the_house = None
        house.out_house(self.name)


class House:

    def __init__(self, address):
        self.address = address
        self.a_list = []

    def display(self):
        print('This house is at: {}'.format(self.address))
        if self.a_list != []:
            for each in self.a_list:
                print('\t', each)

    # puts the name in a list of names for that specific house object.
    def in_house(self, name):
        self.a_list.append(name)

    # takes the name out of the list of names for that specific house object.
    def out_house(self, name):
        if name in self.a_list:
            self.a_list.remove(name)
        else:
            print('{} is not in a house'.format(name))


if __name__ == '__main__':
    print('The options are:\n\tcreate <person name>\n\tperson-name enter house-address\n\tperson-name exit house-address\n\tdisplay')
    in_string = input('What do you want to do? ')
    people_list = []
    house_list = []
    while in_string.strip().lower() not in ['quit', 'q']:
        enter_string = in_string.split('enter')
        exit_string = in_string.split('exit')
        if in_string.split()[0:2] == ['create', 'person']:
            people_list.append(Person(' '.join(in_string.split()[2:])))
            print('Person {} created'.format(people_list[-1].name))
        elif in_string.split()[0:2] == ['create', 'house']:
            house_list.append(House(' '.join(in_string.split()[2:])))
            print('House {} created'.format(house_list[-1].address))
        elif len(enter_string) == 2:
            if not any(enter_string[0].strip() == person.name for person in people_list):
                print('The person isn\'t in the list.')
            elif not any(enter_string[1].strip() == house.address for house in house_list):
                print('The house isn\'t in the list.')
            else:
                the_house = None
                the_person = None
                for house in house_list:
                    if house.address == enter_string[1].strip():
                        the_house = house
                for person in people_list:
                    if person.name == enter_string[0].strip():
                        the_person = person
                if the_person and the_house:
                    the_person.go_in(the_house)
                else:
                    print('Something went wrong.  ')
        elif len(exit_string) == 2:
            if not any(exit_string[0].strip() == person.name for person in people_list):
                print('The person isn\'t in the list.')
            elif not any(exit_string[1].strip() == house.address for house in house_list):
                print('The person isn\'t in the list.')
            else:
                the_house = None
                the_person = None
                for house in house_list:
                    if house.address == exit_string[1].strip():
                        the_house = house
                for person in people_list:
                    if person.name == exit_string[0].strip():
                        the_person = person
                if the_person and the_house:
                    the_person.leave(the_house)
                else:
                    print('Something went wrong.  ')
        elif in_string.lower().strip() == 'display':
            for house in house_list:
                house.display()
            print('These people aren\'t in a house')
            for person in people_list:
                if not person.the_house:
                    print(person.name)

        in_string = input('What do you want to do? ')
