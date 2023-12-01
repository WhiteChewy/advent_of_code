"""Author: Nikita Kulikov (c) 01.12.2023

Advent Of Code first day. 1/2 puzzle.
"""
import functools
import re

from typing import Iterator

numbers = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
    }


def find_first_subline_digits(line: str) -> Iterator:
    """Get tuple of first and last name of digit in text from line. F.e. ((3, 'one'), (89, 'six'))"""
    max_index = (0,)
    min_index = (len(line), )
    # Find every occurence for digit name in line
    for i in numbers:
        occurences = re.finditer(i, line)
        indexes = functools.reduce(lambda x, y: x+[y.start()], occurences, [])
        # Checking if this is the first or last occurence of name
        for index in indexes:
            if index > max_index[0]:
                max_index = (index, i)
            if index < min_index[0]:
                min_index = (index, i)
    # if max_index and min_index are the same then return None
    if max_index == (0, ) and min_index == (len(line), ):
        return None
    # else if only min_index changes then this name has one occurence
    elif max_index == (0, ):
        return (min_index, min_index)
    # if both changes return them
    else:
        return (min_index, max_index)

def first_number(line: list) -> int:
    """Get first number in line."""
    iterator = filter(lambda ch: ch if ch.isdigit() else None, line)
    # If first element exist in iterator return it if not return None
    try:
        return next(iterator)
    except StopIteration:
        return None

def filter_calibration_number(line: str) -> int:
    """Get calibration number for line."""
    chars = list(line)
    is_there_names = find_first_subline_digits(line)
    if is_there_names is not None:
        first_digit_name, last_digit_name = is_there_names
        # If there is digits BEFORE first name of digit -- then this is the first digit in string
        there_number_before = bool(first_digit_name[0] and first_number(line[:first_digit_name[0]]))
        # If there is digits AFTER END of names of digit -- then this is the last digit in string
        there_number_after = bool(line[:last_digit_name[0] + len(last_digit_name[1]):-1]
                                # get substring after the name of digit and check if there is some digits
                                and first_number(line[:last_digit_name[0] - 1 + len(last_digit_name[1]):-1]))
        first_digit = first_number(chars) if there_number_before else numbers[first_digit_name[1]]
        last_digit = first_number(chars[::-1]) if there_number_after else numbers[last_digit_name[1]]
    else:
        first_digit = first_number(chars)
        last_digit = first_number(chars[::-1])
    return int(first_digit + last_digit)


def get_calibration_nubers_sum(filename: str='01_12_2023/input.txt'):
    with open(filename, 'r') as file:
        lines = file.readlines()
    calibration_numbers = map(filter_calibration_number, lines)
    return functools.reduce(lambda x, y: x+y, calibration_numbers)

if __name__ == '__main__':
    result = get_calibration_nubers_sum()
    print(result)
