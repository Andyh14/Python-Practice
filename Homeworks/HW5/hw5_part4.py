"""
File:         hw5_part4.py
Author:       Andy Huang
Date:         10/14/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program makes two creates in a .json file fight each other and finds who wins the fight.
"""


def read_creature_file(creature_file_name):
    """
    :param creature_file_name: a json file with creature stats.
    :return: a python dictionary of creatures.
    """
    import json
    try:
        with open(creature_file_name) as f:
            return json.loads(f.read())
    except OSError:
        print('Unable to open the file, is it in the right place? ')

    return {}


def fight_creatures(first_to_attack, second_to_attack):
    """
    This should fight the two creatures.

    It should create and set an "alive" element in their dictionaries and if the creature is killed, set it to False.
    Each creature deals damage to the other, unless one has first strike, the other doesn't, and the creature with first strike deals fatal damage.
    Then the first strike creature does not receive damage.

    :param first_to_attack:
    :param second_to_attack:
    :return:
    """
    # puts the alive key into the creatures dictionary.
    first_to_attack['alive'] = True
    second_to_attack['alive'] = True

    # first strike battle calculations. If health is below zero change alive to False.
    if first_to_attack['first_strike']:
        after_battle_second_creature_health = second_to_attack['life'] - first_to_attack['attack']
        if after_battle_second_creature_health <= 0:
            second_to_attack['alive'] = False

    if second_to_attack['first_strike']:
        after_battle_first_creature_health = first_to_attack['life'] - second_to_attack['attack']
        if after_battle_first_creature_health <= 0:
            first_to_attack['alive'] = False

    # normal battle calculations
    if first_to_attack['alive'] and second_to_attack['alive']:
        first_creature_life_after_battle = first_to_attack['life'] - second_to_attack['attack']
        second_creature_life_after_battle = second_to_attack['life'] - first_to_attack['attack']

        if first_creature_life_after_battle <= 0:
            first_to_attack['alive'] = False

        if second_creature_life_after_battle <= 0:
            second_to_attack['alive'] = False
    return


if __name__ == '__main__':
    creatures = read_creature_file(input('What creature file do you want to load? '))
    if creatures:
        while input('Fight again? ').strip().lower() in ['yes', 'y']:
            first_creature_name = input('What is the first creature? ')
            second_creature_name = input('What is the second creature? ')
            if first_creature_name in creatures and second_creature_name in creatures:
                first_creature = creatures[first_creature_name]
                second_creature = creatures[second_creature_name]
                fight_creatures(first_creature, second_creature)
                # hint, are these magic values? hmm... should you do this in your own code?
                print(first_creature_name, first_creature['attack'], first_creature['life'], first_creature['alive'])
                print(second_creature_name, second_creature['attack'], second_creature['life'],
                      second_creature['alive'])

                if first_creature['alive']:
                    print(first_creature_name, 'has survived the fight. ')
                else:
                    print(first_creature_name, 'has died in the fight. ')
                if second_creature['alive']:
                    print(second_creature_name, 'has survived the fight. ')
                else:
                    print(second_creature_name, 'has died in the fight. ')
            else:
                print('One of the creatures wasn\'t in the list of creatures')
