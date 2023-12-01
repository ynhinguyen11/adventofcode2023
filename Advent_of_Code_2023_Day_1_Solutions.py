# -*- coding: utf-8 -*-
"""
Advent of Code Day 1 Solutions
Day 1 puzzle prompts reference: https://adventofcode.com/2023/day/1
    
Created on Fri Dec  1 12:52:42 2023

@author: ynhin
"""

import pandas as pd
import os
import itertools


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
    try:
        calibration_value = int("".join(extracted_numbers[::len(extracted_numbers)-1]))
    except ValueError:
        # The digit duplicates to make two digits when only one digit exists
        calibration_value = int(extracted_numbers[0] + extracted_numbers[0])
        
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
    
    # Search through the string from the first character to the 3rd from last character
    # in sections of 3 - 5 characters length for numeric words
    str_length = len(calibration)
    for str_start, str_range in itertools.product(range(0,str_length-1), [3,4,5]):
        str_end = str_start + str_range
        # Skip any end position that is greater than the string length minus 1
        if  str_end > str_length:
            continue
        # Replace numeric words with number
        for numeric_word in num_dict:
            if numeric_word in calibration[str_start:str_end]:
                # Add in the last letter of the numeric word with the number
                # in case the last letter connects to another numeric word
                # For example: eightwo = 82
                calibration = calibration.replace(numeric_word, 
                                                  num_dict[numeric_word] + 
                                                  calibration[str_start:str_end][-1])
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
        'nine': '9',
        'eight': '8',
        'seven': '7',
        'six': '6',
        'five': '5',
        'four': '4',
        'three': '3',
        'two': '2',
        'one': '1'}
    for calibration in calibration_doc[0]:
        sum_calibration_value = day1_part2_replace_numeric_words_with_numbers(
            sum_calibration_value, calibration, num_dict)
    print('The sum of the new calibration values = %d' %sum_calibration_value)
    
    
if __name__ == "__main__":
    main()
    
