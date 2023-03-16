"""
File:         hw5_part1.py
Author:       Andy Huang
Date:         10/13/2020
Section:      46
E-mail:       andyh1@umbc.edu
Description:  This program takes in a string of nucleotides and returns a list of genes, if there are any...
"""

import sys
from random import choice, seed


if len(sys.argv) >= 2:
    seed(sys.argv[1])

# USE IF YOU ARE TESTING AND DON'T WANT TO USE COMMAND LINE ARGUMENTS
# seed(input('What seed do you want to use? '))
# END SECTION

STOP_PARAM = 'stop'
SEQ_PARAM = 'seq'
NUCLEOTIDES = ['A', 'T', 'C', 'G']
# your constants should start here
START = ['ATG']
STOP = ['TAA', 'TGA', 'TAG']
CODON_LENGTH = 3
MAIN_QUESTION = 'How many codons do you want to create? (or stop to end, seq to enter your own sequence) '


def extract_genes(the_sequence):
    """
    This function should return a list of genes that start with the
    start codon and end with one of the three stop codons.
    :param the_sequence: a string of nucleotides
    :return: a list of "genes"
    """
    empty_list = []
    stop_looping = 0

    # loop counts through in triplets
    for starting_index in range(0, len(the_sequence), CODON_LENGTH):
        empty_string = ''
        triplet = the_sequence[starting_index: starting_index + CODON_LENGTH]

        # checks if the codon is a starting codon and starts the loop.
        if triplet in START:
            stop_looping += 1

            # checks if the codon after the starting codon is a stopping codon.
            for ending_index in range(starting_index + CODON_LENGTH, len(the_sequence), CODON_LENGTH):
                if stop_looping % 2 != 0:
                    ending_triplet = the_sequence[ending_index: ending_index + CODON_LENGTH]

                    # appends the sequence from the start of the starting codon to the end of the ending triplet.
                    if ending_triplet in STOP:
                        empty_string += the_sequence[starting_index: ending_index + CODON_LENGTH]

                        empty_list.append(empty_string)
                        stop_looping += 1
    return empty_list


if __name__ == '__main__':
    length_or_stop = input(MAIN_QUESTION)
    while length_or_stop.lower() != STOP_PARAM:
        try:
            if length_or_stop.lower() == SEQ_PARAM:
                sequence = input('Enter your own sequence: ').upper()
                if len(sequence) % 3 != 0:
                    raise ValueError('The length of the string must be divisible by 3')
                if any(x not in NUCLEOTIDES for x in sequence):
                    raise ValueError('The sequence must contain only A, T, C, G')
            else:
                sequence = ''.join([choice(NUCLEOTIDES) for _ in range(3 * int(length_or_stop))])
            print(sequence)
            print(extract_genes(sequence))
        except ValueError:
            print('You entered a non-STOP non-integer, try again. ')
        length_or_stop = input(MAIN_QUESTION)
