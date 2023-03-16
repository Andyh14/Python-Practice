"""
File:         hw2_part3.py
Author:       Andy Huang
Date:         9/15/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program will try to guess what Star trek character the user is thinking of by
asking a series of questions.

"""

question_human = input("Is the character human (at least partially)? ")

if question_human.lower() == "yes":
    question_bald = input("Is the character bald? ")
    if question_bald.lower() == "yes":
        print('You are thinking of Captain Picard')
    else:
        question_empath = input('Is this person an empath? ')
        if question_empath.lower() == "yes":
            print('You are thinking of Counselor Troi ')
        else:
            question_blind = input('Is this person blind? ')
            if question_blind.lower() == "yes":
                print("You are thinking of Geordi.")
            else:
                question_number_1 = input("Are they number 1? ")
                if question_number_1.lower() == "yes":
                    print('You are thinking of Riker.')
                else:
                    print("Shut up Wesley.")
else:
    question_klingon = input("Is the person Klingon? ")
    if question_klingon.lower() == "yes":
        print("You are thinking about Worf. ")
    else:
        question_android = input("Are they a android? ")
        if question_android.lower() == "yes":
            print("You are thinking about Data. ")
        else:
            print('I don\'t know, Mot the Barber maybe?')















