"""
File:    pyopoly.py
Author:  Andy Huang
Date:    10/29/2020
Section: 46
E-mail:  Andyh1@umbc.edu
Description:
  This program is like the well known board game Monopoly, but a little different. The goal is to survive longer
  than your opponent. That is, to not go bankrupt!
"""

from sys import argv
from random import randint, seed
from board_methods import load_map, display_board

if len(argv) >= 2:
    seed(argv[1])

QUIT_STRING = 'quit'
OPTIONS_STRING = "     1) Buy Property \n     2) Get Property Info \n     3) Get Player Info \n     " \
                 "4) Build a Building \n     5) End Turn"
OPTIONS_LIST = ['buy property', 'get property info', 'get player info', 'build a building', 'end turn']
STARTING_MONEY = 1500
PASS_GO_MONEY = 200
NUMBER_OUT_OF_BOARD = 33
BANK_NAME = 'BANK'
YES_CONSTANT = 'yes'
ALREADY_OWNED_STATEMENT = 'This property is already owned or not for sale. You cannot buy it...'
NOT_OWNED_STATEMENT = 'This property is unowned, would you like to buy it? (yes or no)'
GET_PROPERTY_QUESTION = 'For which property do you want to get the information? '
BUILD_BUILDING_QUESTION = 'Which property do you want to build a building on? '


def dice_roll():
    return randint(1, 6) + randint(1, 6)


def player_moving(player_symbol, position_player_one, position_player_two, board):
    """
        :param player_symbol: The symbol of a player
        :param position_player_one: The integer value of the position of a player.
        :param position_player_two: The integer value of the position of a player.
        :param board: The list of dictionaries that is used to display the board.
        :return A copy of the board with the moved symbol.
    """
    copy_board = list(board)

    # the statement stops the symbols from overwriting each other.
    if position_player_one == position_player_two:
        decoy_board = list(the_board)
        mutual_position = position_player_one
        copy_board[mutual_position] = decoy_board[mutual_position][0:6] + (symbol_player_one[0:5] + symbol_player_two[0:5])
    else:
        copy_board[position_player_one] = copy_board[position_player_one][0:6] + player_symbol[0:5]
    return copy_board


def buy_property(player_info, position_of_player, building_costs):
    """
        :param player_info: the dictionary of a player.
        :param position_of_player: The integer value of the position of the player.
        :param building_costs: The list of dictionaries that has the information of the building costs
        :return The new list of dictionaries with changed price and owner name.
    """
    empty_dictionary = {}
    if int(building_costs[position_of_player]['Price']) >= 0:
        purchase = input(NOT_OWNED_STATEMENT)
        if purchase.lower() == YES_CONSTANT:
            if player_info['Money'] - int(building_costs[position_of_player]['Price']) < 0:
                print('You don\'t have enough money to buy this.')
            else:
                # adds the dictionary of the property with the information needed to be shown.
                empty_dictionary['Place'] = building_costs[position_of_player]['Place']
                empty_dictionary['Abbrev'] = building_costs[position_of_player]['Abbrev']
                empty_dictionary['BuildingCost'] = building_costs[position_of_player]['BuildingCost']
                player_info['Property'].append(empty_dictionary)

                # Money transfer while changing the price to -1 and owner.
                player_info['Money'] -= int(building_costs[position_of_player]['Price'])
                building_costs[position_of_player]['Price'] = int(-1)
                building_costs[position_of_player]['Owner'] = player_info['Name']
                print('You have bought {}'.format(building_costs[position_of_player]['Place']))
    else:
        print(ALREADY_OWNED_STATEMENT)

    return building_costs


def get_property_info(board_specifics):
    """
        :param board_specifics: The list of dictionaries containing all the information of the properties.
    """
    specific_property = str(input(GET_PROPERTY_QUESTION))
    print()
    for each in range(len(board_specifics)):

        # checks the user input whether it be the name of the place or the abbreviation.
        if board_specifics[each]['Place'] == specific_property or board_specifics[each]['Abbrev'] == specific_property:
            print('    ', board_specifics[each]['Place'])
            print('     Price:', board_specifics[each]['Price'])
            print('     Owner:', board_specifics[each]['Owner'])
            print('     Building:', board_specifics[each]['Building'])
            print('     Rent {}, {} (with building)'.format(board_specifics[each]['Rent'], board_specifics[each]['BuildingRent']))
    print('\n')


def get_player_info():
    print('The players are \n        {}\n        {}'.format(player_one_dictionary['Name'], player_two_dictionary['Name']))
    specific_player = str(input('Which player do you wish to know about? '))
    
    # prints all the information of the Player if input matches.
    if specific_player.lower() == player_one_dictionary['Name'].lower():
        print('Player name: {}'.format(player_one_dictionary['Name']))
        print('PLayer symbol: {}'.format(player_one_dictionary['Symbol']))
        print('Current money: {}'.format(player_one_dictionary['Money']))
        if len(player_one_dictionary['Property']) == 0:
            print()
            print('               No Properties Yet')
        else:
            print('Properties owned: {}'.format(player_one_dictionary['Property']))

    if specific_player.lower() == player_two_dictionary['Name'].lower():
        print('Player name: {}'.format(player_two_dictionary['Name']))
        print('PLayer symbol: {}'.format(player_two_dictionary['Symbol']))
        print('Current money: {}'.format(player_two_dictionary['Money']))
        if len(player_two_dictionary['Property']) == 0:
            print()
            print('               No Properties Yet')
        else:
            print('Properties owned: {}'.format(player_two_dictionary['Property']))


def build_building(player_info, building_information):
    """
        :param player_info: The dictionary of a player to access the properties a player owns.
        :param building_information: The list of dictionaries containing all the information.
        :return new list of dictionaries with the updated information.
    """
    if len(player_info['Property']) != 0:
        
        # this lists all the properties owned by the player.
        for number in range(len(player_info['Property'])):
            print(player_info['Property'][number]['Place'], player_info['Property'][number]['Abbrev'], player_info['Property'][number]['BuildingCost'])

        building_answer = str(input(BUILD_BUILDING_QUESTION))

        # finding the input in the player property dictionary
        for each in range(len(player_info['Property'])):

            # checking if the input is one of the properties the player owns
            if player_info['Property'][each]['Place'].lower() == building_answer.lower() or player_info['Property'][each]['Abbrev'].lower() == building_answer.lower():

                # makes sure building answer is the full name not the abbreviation.
                building_answer = player_info['Property'][each]['Place']

                # finding the property on the board and checking if there is a building.
                for dash in range(len(building_information)):
                    if building_information[dash]['Place'] == building_answer:
                        if building_information[dash]['Building'] == False:

                            # checking for sufficient funds and if so, buy the building.
                            if player_info['Money'] - int(building_information[dash]['BuildingCost']) > 0:
                                player_info['Money'] -= int(building_information[dash]['BuildingCost'])
                                building_information[dash]['Building'] = True
                                print('You built the building for {}'.format(building_information[dash]['Place']))
                            else:
                                print('You do not have sufficient funds.')
                        else:
                            print('There is already a Building on this property. ')
            else:
                print('That is not a name of a property you own.')
    else:
        print('You do not have any properties yet!')
    return building_information


def play_game(players_dictionary, position, board_info):
    """
        :param players_dictionary: The dictionary of a player
        :param position: The integer value of the position of a player.
        :param board_info: The list of dictionaries with all the information of the board.
        :return The changed board through that might've been changed through the options.
    """
    loop_trigger = True
    while loop_trigger:
        print(OPTIONS_STRING)
        player_decision = input("What will you do? ")

        if str(player_decision).lower() == OPTIONS_LIST[0] or player_decision == '1':
            board_info = buy_property(players_dictionary, position, board_info)

        if str(player_decision).lower() == OPTIONS_LIST[1] or player_decision == '2':
            get_property_info(board_info)

        if str(player_decision).lower() == OPTIONS_LIST[2] or player_decision == '3':
            get_player_info()

        if str(player_decision).lower() == OPTIONS_LIST[3] or player_decision == '4':
            board_info = build_building(players_dictionary, board_info)

        if str(player_decision).lower() == OPTIONS_LIST[4] or player_decision == '5':
            loop_trigger = False
    return board_info


def check_if_losing(lost_player_dictionary, loss_dictionary):
    """
        :param lost_player_dictionary: The dictionary of a player.
        :param loss_dictionary: The dictionary that includes the loss factor so we can change it to True if needed.
        :return The new loss dictionary with possibly the loss factor and the losing player's name.
    """
    if lost_player_dictionary['Money'] <= 0:
        loss_dictionary['Losing Factor'] = True
        loss_dictionary['Player'] = lost_player_dictionary['Name']
    return loss_dictionary


def calculate_rent(position, person_one, person_two, rent_info):
    """
        :param position: The integer value of the position of the spot the person landed on.
        :param person_one: A dictionary of the player who is paying the rent.
        :param person_two: A dictionary of the player who is receiving the rent.
        :param rent_info: The list of dictionaries that holds all the information of the board.
        :return The changed dictionary of player one and player two.
    """
    if rent_info[position]['Building']:
        person_one['Money'] -= int(rent_info[position]['BuildingRent'])
        person_two['Money'] += int(rent_info[position]['BuildingRent'])
    else:
        if rent_info[position]['Owner'].lower() != BANK_NAME.lower():
            person_one['Money'] -= int(rent_info[position]['Rent'])
            person_two['Money'] += int(rent_info[position]['Rent'])
    return person_one, person_two


def starting_info(a_dictionary, a_name, a_symbol):
    """
        :param a_dictionary: any dictionary to add the starting info to.
        :param a_name: the name to assign into the dictionary.
        :param a_symbol: the symbol to assign into the dictionary.
        :return the changed dictionary
    """
    a_dictionary['Name'] = str(a_name)
    a_dictionary['Symbol'] = str(a_symbol)
    a_dictionary['Money'] = int(STARTING_MONEY)
    a_dictionary['Property'] = []
    return a_dictionary


if __name__ == '__main__':

    player_one_dictionary = {}
    player_two_dictionary = {}

    # getting user input for player 1
    name_player_one = input('First player, what is your name? ')
    symbol_player_one = str(input('First player, what is the symbol you want your character to use? '))
    while len(symbol_player_one) != 1 or ord(symbol_player_one) > 91 or ord(symbol_player_one) < 64:
        print('Please use one of any uppercase letter as your symbol. \n ')
        symbol_player_one = str(input('First player, what is the symbol you want your character to use? '))

    # getting user input for player 2
    name_player_two = input('Second player, what is your name? ')
    symbol_player_two = str(input('Second player, what is the symbol you want your character to use? '))
    while len(symbol_player_two) != 1 or ord(symbol_player_two) > 91 or ord(symbol_player_two) < 64 or symbol_player_one == symbol_player_two:
        print('Please use one of any uppercase letter that is different from player one as your symbol. \n ')
        symbol_player_two = str(input('Second player, what is the symbol you want your character to use? '))

    # creating player one's dictionary with their information.
    starting_info(player_one_dictionary, name_player_one, symbol_player_one)

    # creating player two's dictionary with their information.
    starting_info(player_two_dictionary, name_player_two, symbol_player_two)

    board_information = load_map('proj1_board1.csv')

    for dictionary in board_information:
        dictionary['Owner'] = BANK_NAME
        dictionary['Building'] = False

    the_board = []
    for i in range(32):
        the_board.append(((load_map('proj1_board1.csv')[i]["Abbrev"][0:5]) + "\n"))

    position_one = 0
    position_two = 0
    losing_info = {'Losing Factor': False}
    players_board = list(the_board)

    while losing_info['Losing Factor'] == False:

        first_player_move = 5
        position_one += first_player_move

        # gives pass go money when passing index zero or goes over it for player one
        if position_one >= 32:
            player_one_dictionary['Money'] += PASS_GO_MONEY
        position_one %= len(the_board)

        # shows player two at GO at the start of the game
        if position_two == 0:
            players_board = player_moving(symbol_player_two, position_two, position_one, the_board)

        display_board(player_moving(symbol_player_one, position_one, position_two, players_board))

        # changes players board accordingly depending to prevent unwanted symbols.
        if position_one != position_two:
            players_board = player_moving(symbol_player_one, position_one, position_two, the_board)
        else:
            players_board = player_moving(symbol_player_one, position_one, NUMBER_OUT_OF_BOARD, players_board)

        print('{} you rolled a {}'.format(name_player_one, first_player_move))
        print('{} you landed on {}'.format(name_player_one, load_map('proj1_board1.csv')[position_one]["Place"]))

        # checking functions for winning or losing the game
        calculate_rent(position_one, player_one_dictionary, player_two_dictionary, board_information)

        check_if_losing(player_one_dictionary, losing_info)

        # if statement lets me end the game the moment any player goes bankrupt
        if losing_info['Losing Factor'] == False:
            board_information = play_game(player_one_dictionary, position_one, board_information)

        # second players turn
            second_player_move = 5
            position_two += second_player_move

            # gives pass go money when passing index zero or goes over it for player two
            if position_two >= 32:
                player_two_dictionary['Money'] += PASS_GO_MONEY
            position_two %= len(the_board)

            display_board(player_moving(symbol_player_two, position_two, position_one, players_board))

            # changes players board accordingly depending to prevent unwanted symbols.
            if position_one != position_two:
                players_board = player_moving(symbol_player_two, position_two, position_one, the_board)
            else:
                players_board = player_moving(symbol_player_two, position_two, NUMBER_OUT_OF_BOARD, the_board)

            print('{} you rolled a {}'.format(name_player_two, second_player_move))
            print('{} you landed on {}'.format(name_player_two, load_map('proj1_board1.csv')[position_two]["Place"]))

            calculate_rent(position_two, player_two_dictionary, player_one_dictionary, board_information)

            check_if_losing(player_two_dictionary, losing_info)

            if losing_info['Losing Factor'] == False:
                board_information = play_game(player_two_dictionary, position_two, board_information)

    print('{} went bankrupt and lost the game... \n'.format(losing_info['Player']))

    if str(losing_info['Player']).lower() == name_player_one:
        print('{}, Congratulations! You won!!'.format(name_player_two))
    else:
        print('{}, Congratulations! You have won!!'.format(name_player_one))
