"""
File:         hw3_part5.py
Author:       Andy Huang
Date:         9/23/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program will determine the point on the Eightfold Path in Buddhism given a angle degree.

"""
if __name__ == "__main__":

    eightfold_path_angle = int(input('Enter a angle to determine the point on the Eightfold Path: '))

    path_list = ['Right Resolve', 'Right View', 'Right Samadhi', 'Right Mindfulness', 'Right Effort',
                 'Right Livelihood','Right Conduct', 'Right Speech']

    # checks if the input is divisible by 45
    if eightfold_path_angle % 45 == 0:

        true_angle = eightfold_path_angle // 45

        angle_to_list = true_angle % 8

        print('You have selected', path_list[angle_to_list])

    else:
        print('You have not reached enlightenment yet, try an angle divisible by 45.')






