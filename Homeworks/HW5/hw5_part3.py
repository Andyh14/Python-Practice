"""
File:         hw5_part3.py
Author:       Andy Huang
Date:         10/14/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program takes a 2D room and returns an updated room with the path the robot took.
"""
DOT = '.'
FREE_SPACE = ''


def print_robo_array(room):
    for row in room:
        for x in row:
            if not x:
                print(DOT.ljust(3), end=' ')
            else:
                print(str(x).ljust(3), end=' ')
        print()
    print()


def robo_vac(room, starting_y, starting_x):
    """
    Compute a path through the room for the robot vacuum.

    :param room: a 2d-grid representing the room,
                '' blank strings are open spaces
    :param starting_y: starting row (first index)
    :param starting_x: starting column (second index)
    :return: the updated room with the numbers.
    """
    count = 1
    stop_looping = 1
    while stop_looping != 0:

        # check if the checked index is in the range and if so places a value there and moves the position.
        if (starting_x + 1) < len(room[starting_x]) and room[starting_y][starting_x + 1] == FREE_SPACE:

            # put the number down and move the bot
            room[starting_y][starting_x] = count
            starting_x += 1
            count += 1

        # checks down (if the index is off the board do nothing.
        elif (starting_y + 1) < len(room[starting_y]) and room[starting_y + 1][starting_x] == FREE_SPACE:
            room[starting_y][starting_x] = count
            starting_y += 1
            count += 1

        # checks left (if the index is off the board do nothing)
        elif (starting_x - 1) > -1 and room[starting_y][starting_x - 1] == FREE_SPACE:
            room[starting_y][starting_x] = count
            starting_x -= 1
            count += 1

        # checks up (if the index to go up is off the board do nothing)
        elif (starting_y - 1) > -1 and room[starting_y - 1][starting_x] == FREE_SPACE:
            room[starting_y][starting_x] = count
            starting_y -= 1
            count += 1

        # stop the loop and make the last index a number
        else:
            room[starting_y][starting_x] = count
            stop_looping = 0
    return room


if __name__ == '__main__':
    my_room = [['' for _ in range(6)] for _ in range(6)]
    print_robo_array(robo_vac(my_room, 0, 0))
    my_room_with_obstacles = [['' for _ in range(6)] for _ in range(6)]

    for i in range(3, 5):
        for j in range(3, 5):
            my_room_with_obstacles[i][j] = 'x'
    print_robo_array(robo_vac(my_room_with_obstacles, 0, 0))

    my_smaller_room = [['', '', ''], ['', 'x', 'x'], ['', '', 'x']]
    print_robo_array(robo_vac(my_smaller_room, 0, 0))
    my_smaller_room = [['', '', ''], ['', 'x', 'x'], ['', '', 'x']]
    print_robo_array(robo_vac(my_smaller_room, 0, 2))

    another_room = [
        ['', 'x', '', '', '', '', '', ''],
        ['', 'x', 'x', '', 'x', '', 'x', ''],
        ['', 'x', '', '', 'x', 'x', '', ''],
        ['', '', '', '', 'x', '', 'x', ''],
        ['', '', 'x', '', 'x', '', 'x', ''],
        ['', '', 'x', '', 'x', '', 'x', ''],
        ['', '', '', '', 'x', '', 'x', ''],
        ['', '', '', '', '', '', '', '']
    ]
    print_robo_array(robo_vac(another_room, 0, 0))
