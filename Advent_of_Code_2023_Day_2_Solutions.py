# -*- coding: utf-8 -*-
"""
Advent of Code Day 2 Solutions
Day 2 puzzle prompts reference: https://adventofcode.com/2023/day/2

Created on Sat Dec  2 15:42:41 2023

@author: ynhin
"""

import pandas as pd
import os


def extract_number_from_string(string):
    """
    Function to extract the numbers in a string and join each extraction
    into one number. 

    Parameters
    ----------
    string : STR
        AN ALPHANUMERIC STRING INPUT.

    Returns
    -------
    extract_number : INT
        NUMBER FROM THE INPUT STRING.

    """
    extract_number = int("".join([str(character) for character in string if character.isdigit()]))
    return extract_number


def clean_data(game_record, constraints):
    """
    Rename dataframe columns, split results into a list for each row, and create
    3 columns of the max number for each color.

    Parameters
    ----------
    game_record : DATAFRANE
        RAW DATA FROM INPUT FILE WITH TWO COLUMNS.
        DATA DICTIONARY:
            COLUMN 0 - GAME ID
            COLUMN 1 - RESULTS FOR EACH GAME
    constraints : DICTIONARY
        DICTIONARY OF THE POSSIBLE COLORS FOR EACH GAME AND
        THE LIMIT VALUE FOR A POSSIBLE GAME FROM EACH COLOR.

    Returns
    -------
    game_record : DATAFRAME
        CLEANED DATAFRAME WITH MAXIMUM VALUE FOR EACH COLOR IN EACH GAME.
        DATA DICTIONARY:
            GAME_NUMBER - GAME ID
            RESULTS - RESULTS FOR EACH GAME
            RED_MAX - MAX VALUE OF RED IN EACH GAME
            GREEN_MAX - MAX VALUE OF GREEN IN EACH GAME
            BLUE_MAX - MAX VALUE OF BLUE IN EACH GAME

    """
    # Rename columns
    game_record.rename(columns={0: "game_number", 1: "results"}, inplace=True)
    # Make game column numeric
    game_record['game_number'] = list(map(lambda game_num: extract_number_from_string(game_num),
                                          game_record.game_number))
    # Split game into individual result
    game_record['results'] = game_record['results'].str.replace(';', ',').str.split(', ')
    
    # Get max number for each color
    for color in constraints:
        game_record[color + '_max'] = list(map(lambda game: max(
            [extract_number_from_string(result) for result in game if result.find(color) > -1]),
            game_record.results))
    return game_record


def day2_part1_sum_possible_games(game_record, constraints):
    """
    Filter for only possible games i.e. Games within the constraints for each color.
    Then, sum the ID of all possible games.
    
    Parameters
    ----------
    game_record : DATAFRAME
        CLEANED DATAFRAME WITH MAXIMUM VALUE FOR EACH COLOR IN EACH GAME.
        DATA DICTIONARY:
            GAME_NUMBER - GAME ID
            RESULTS - RESULTS FOR EACH GAME
            RED_MAX - MAX VALUE OF RED IN EACH GAME
            GREEN_MAX - MAX VALUE OF GREEN IN EACH GAME
            BLUE_MAX - MAX VALUE OF BLUE IN EACH GAME
    constraints : DICTIONARY
        DICTIONARY OF THE POSSIBLE COLORS FOR EACH GAME AND
        THE LIMIT VALUE FOR A POSSIBLE GAME FROM EACH COLOR.

    Returns
    -------
    possible_sum : INT
        SUM OF ALL GAME IDS THAT MET THE CONSTRAINTS .

    """
    # Filter based on max number against constraints
    game_record_possible = game_record
    for color in constraints:
        game_record_possible = game_record_possible[
            game_record_possible[color +"_max"] <= constraints[color]]
    
    # Sum game number of possible games i.e. games that fall within the constraints
    possible_sum = sum(game_record_possible.game_number)
    return possible_sum


def day2_part2_sum_power(game_record):
    """
    Create a column for power by multiplying the max values for each color and
    sum the calculated power for all games.

    Parameters
    ----------
    game_record : DATAFRAME
        CLEANED DATAFRAME WITH MAXIMUM VALUE FOR EACH COLOR IN EACH GAME.
        DATA DICTIONARY:
            GAME_NUMBER - GAME ID
            RESULTS - RESULTS FOR EACH GAME
            RED_MAX - MAX VALUE OF RED IN EACH GAME
            GREEN_MAX - MAX VALUE OF GREEN IN EACH GAME
            BLUE_MAX - MAX VALUE OF BLUE IN EACH GAME

    Returns
    -------
    power_sum : INT
        SUM OF ALL CALCULATED POWER .

    """
    # Multiply max of each color to get power for each game
    game_record['power'] = game_record['red_max'] * game_record['green_max']* game_record['blue_max']
    
    # Sum the calculated power for all games
    power_sum = sum(game_record.power)
    return power_sum


def main():
    # Load input
    game_record = pd.read_csv(('C:/Users/{}/OneDrive/Desktop/adventofcode2023/' +
                              'Inputs/inputday2.txt').format(os.environ.get('USERNAME')),
                              header=None, sep=':')
    # Specify constraints
    constraints = {'red': 12,
                  'green': 13,
                  'blue': 14}
    game_record = clean_data(game_record, constraints)
    
    possible_sum = day2_part1_sum_possible_games(game_record, constraints)
    print('The sum of game number for possible games = {}'.format(possible_sum))
    
    power_sum = day2_part2_sum_power(game_record)
    print('The sum of power for all games = {}'.format(power_sum))


if __name__ == "__main__":
    main()