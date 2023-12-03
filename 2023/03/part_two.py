"""Author: Nikita Kulikov (c) 03.12.2023

Advent Of Code second day. 2/2 puzzle.
"""
import re
import functools
from typing import List, Tuple, Optional

def find_gear_ratio(x: Tuple[int, int], y: Tuple[int, int], lines: List[str]) -> Optional[tuple]:
    """Check if this asterisk is gear and if it is returns ratio. If not returns None"""
    numbers_pattern = re.compile('[0-9]+')
    gear = []
    for i in range(y[0], y[1]+1):
        numbers_coords = [(number.start(), number.end()) for number in re.finditer(numbers_pattern, lines[i])]
        for coord in numbers_coords:
            set_number = {elem for elem in range(coord[0], coord[1])}
            set_pos = {elem for elem in range(x[0], x[1])}
            if set_number.intersection(set_pos):
                gear.append(int(lines[i][coord[0]: coord[1]]))
    if len(gear) == 2:
        return gear[0]*gear[1]
    else:
        return None


def find_sum_of_gear_ratios(lines: List[str]) -> list:
    """Finding sum of all gear ratios.

    We find '*'. We gets it horizontal position. After it we get [pos-1; pos+1] - this is the range where at least 1
    digit of a number must be. So we check if [pos-1; pos+1] inside of [start; end] of two digits in line of '*',
    line before and line after. And if it is then we find ratio and sum it to result.
    """
    result = 0
    pattern = re.compile('\*')
    for index, line in enumerate(lines):
        asterisk_coord = [(number.start(), number.end()) for number in re.finditer(pattern, line)]
        for start, end in asterisk_coord:
            y_range_start = index - 1 if index else index
            y_range_end = index + 1 if index != len(lines)-1 else index
            x_range_start = start - 1 if start else start
            x_range_end = end + 1 if end != len(lines) else end
            gear_ratio = find_gear_ratio((x_range_start, x_range_end), (y_range_start, y_range_end), lines)
            if gear_ratio:
                result += gear_ratio
    return result


def get_lines(filename: str) -> list:
    """Reading the input file."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

if __name__ == '__main__':
    lines = [line.strip() for line in get_lines('2023/03/input.txt')]
    print(find_sum_of_gear_ratios(lines))