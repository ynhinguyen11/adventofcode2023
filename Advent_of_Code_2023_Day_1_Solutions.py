# -*- coding: utf-8 -*-
"""
Advent of Code Day 1 Solutions
Day 1 puzzle prompts reference: https://adventofcode.com/2023/day/1
    
Created on Fri Dec  1 12:52:42 2023

@author: ynhin
"""

import pandas as pd
import os


def day1_part1_extract_numbers_in_string(sum_calibration_value, calibration):
    """
    Function to extract numbers from a string, combine the first and last number found
    into a two digits value, and sum the two digits value to the total

    Parameters
    ----------
    sum_calibration_value : INT
        Sum value of the calibration values so far.
    calibration : STR
        Alphanumeric string that contains the calibration value.

    Returns
    -------
    sum_calibration_value : INT
        Sum value of the current and previous calibration values.

    """
        
    # Extract numbers from string
    extracted_numbers = [str(character) for character in calibration if character.isdigit()]
    
    # Join only the first and last element in the list to make the two digits value
    calibration_value = int(extracted_numbers[0] + extracted_numbers[-1])
        
    # Sum all calibration values
    sum_calibration_value += calibration_value
    
    return sum_calibration_value


def day1_part2_replace_numeric_words_with_numbers(sum_calibration_value, calibration, num_dict):
    """
    Function to identify and replace numeric words with corresponding numbers
    from left to right in a string, extract numbers from a string, 
    combine the first and last number found into a two digits value, 
    and sum the two digits value to the total.

    Parameters
    ----------
    sum_calibration_value : INT
        SUM VALUE OF THE CALIBRATION VALUES SO FAR.
    calibration : STR
        ALPHANUMERIC STRING THAT CONTAINS THE CALIBRATION VALUE.
    num_dict : DICTIONARY
        DICTIONARY OF NUMERIC WORDS WITH THEIR CORRESPONDING NUMBERS FOR 1 - 9.

    Returns
    -------
    sum_calibration_value : INT
        SUM VALUE OF THE CURRENT AND PREVIOUS CALIBRATION VALUES.

    """

    # Replace numeric words with number
    for numeric_word in num_dict:
        if numeric_word in calibration:
            calibration = calibration.replace(numeric_word, num_dict[numeric_word])
            
    # Extract, create, and sum the calibration values
    sum_calibration_value = day1_part1_extract_numbers_in_string(sum_calibration_value, calibration)
        
    return sum_calibration_value

    
def main():
    #Load input
    calibration_doc = pd.read_csv(('C:/Users/{}/OneDrive/Desktop/adventofcode2023/' +
                                  'Inputs/inputday1.txt').format(os.environ.get('USERNAME')),
                                  header=None)
    
    # --------- Part 1 ---------------------------------------
    # Find the number(s) in each line to figure out the calibration value 
    # in the calibration document and get the sum of the calibration values 
    # so the elves can send you to the sky to help them solve the global snow
    # production problem.
    # --------------------------------------------------------
    sum_calibration_value = 0
    for calibration in calibration_doc[0]:
        sum_calibration_value = day1_part1_extract_numbers_in_string(sum_calibration_value,
                                                                     calibration)
    print('The sum of the calibration values = %d' %sum_calibration_value)
    
    
    # --------- Part 2 ---------------------------------------
    # Do the same thing as part 1 except also consider the numeric words in
    # each line to figure out the calibration value.
    # --------------------------------------------------------
    sum_calibration_value = 0
    # Create a dictionary to convert numeric words to numbers.
    # Did not include numeric words higher than 9 because data doesn't contain those words
    # Checked if data contains 'ty', 'teen', 'eleven', 'twelve', 'thirteen', & 'ten'
    num_dict={
        'nine': 'n9e',
        'eight': 'e8t',
        'seven': 's7n',
        'six': 's6x',
        'five': 'f5e',
        'four': 'f4r',
        'three': 't3e',
        'two': 't2o',
        'one': 'o1e'}
    for calibration in calibration_doc[0]:
        sum_calibration_value = day1_part2_replace_numeric_words_with_numbers(
            sum_calibration_value, calibration, num_dict)
    print('The sum of the new calibration values = %d' %sum_calibration_value)
    
    
if __name__ == "__main__":
    main()
    
