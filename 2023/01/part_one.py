"""Author: Nikita Kulikov (c) 01.12.2023

Advent Of Code first day. 1/2 puzzle.
"""
import functools


def first_number(line: list) -> int:
    """Get first number in line."""
    iterator = filter(lambda ch: ch if ch.isdigit() else None, line)
    return next(iterator)

def filter_calibration_number(line: str) -> int:
    """Get calibration number for line."""
    chars = list(line)
    return int(first_number(chars) + first_number(chars[::-1]))


def get_calibration_nubers_sum(filename: str='01_12_2023/input.txt'):
    with open(filename, 'r') as file:
        lines = file.readlines()
    calibration_numbers = map(filter_calibration_number, lines)
    return functools.reduce(lambda x, y: x+y, calibration_numbers)

if __name__ == '__main__':
    result = get_calibration_nubers_sum()
    print(result)
