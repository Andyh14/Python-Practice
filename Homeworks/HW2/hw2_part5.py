"""
File:         hw2_part5.py
Author:       Andy Huang
Date:         9/15/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program will determine the point on the Eightfold Path in Buddhism given a angle degree.


"""
eightfold_path_angle = int(input('Enter a angle to determine the point on the Eightfold Path: '))

if eightfold_path_angle > 360:
    angle = eightfold_path_angle % 360
    if angle == 0:
        print('You have selected Right Resolve.')
    if angle // 45 == 1:
        print('You have selected Right View')
    if angle // 45 == 2:
        print('You have selected Right Samadhi')
    if angle // 45 == 3:
        print('You have selected Right Mindfulness')
    if angle // 45 == 4:
        print('You have selected Right Effort')
    if angle // 45 == 5:
        print('You have selected Right Livelihood')
    if angle // 45 == 6:
        print('You have selected Right Conduct')
    if angle // 45 == 7:
        print('You have selected Right Speech')
    if angle // 45 == 8:
        print('You have selected Right Resolve')

if eightfold_path_angle % 45:
    print('You have not reached enlightenment yet, try an angle divisible by 45. ')
else:
    if eightfold_path_angle == 0:
        print('You have selected Right Resolve')
    if eightfold_path_angle // 45 == 1:
        print('You have selected Right View')
    if eightfold_path_angle // 45 == 2:
        print('You have selected Right Samadhi')
    if eightfold_path_angle // 45 == 3:
        print('You have selected Right Mindfulness')
    if eightfold_path_angle // 45 == 4:
        print('You have selected Right Effort')
    if eightfold_path_angle // 45 == 5:
        print('You have selected Right Livelihood')
    if eightfold_path_angle // 45 == 6:
        print('You have selected Right Conduct')
    if eightfold_path_angle // 45 == 7:
        print('You have selected Right Speech')
    if eightfold_path_angle // 45 == 8:
        print('You have selected Right Resolve')






















