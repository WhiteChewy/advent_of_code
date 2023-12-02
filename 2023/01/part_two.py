"""Author: Nikita Kulikov (c) 01.12.2023

Advent Of Code first day. 2/2 puzzle.
"""
import functools
import re

from typing import Iterator

def find_first_subline_digits(line: str) -> Iterator:
    """Get first and last number for line"""
    # List of target values
    list_of_names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # decoder for numbers
    decoder = {w: str(i%9+1) for i, w in enumerate(list_of_names)}
    # find first occure of values from list_of_names with this regex
    first_pattern = re.compile('(' + '|'.join(list_of_names)+')')
    # find last occure of values from list_of_names with this regex
    last_pattern = re.compile('.*(' + '|'.join(list_of_names)+')')
    # find last and first digit
    first_num = decoder[first_pattern.search(line).groups()[0]]
    last_num = decoder[last_pattern.search(line).groups()[0]]
    return int(first_num + last_num)


def get_calibration_nubers_sum(filename: str='2023/01_12_2023/input.txt'):
    with open(filename, 'r') as file:
        lines = file.readlines()
    calibration_numbers = map(find_first_subline_digits, lines)
    return functools.reduce(lambda x, y: x+y, calibration_numbers)

if __name__ == '__main__':
    result = get_calibration_nubers_sum()
    print(result)
