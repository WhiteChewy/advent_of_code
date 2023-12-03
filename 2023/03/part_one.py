"""Author: Nikita Kulikov (c) 03.12.2023

Advent Of Code second day. 1/2 puzzle.
"""
import re
import functools

def is_number_valid(sub_string: str) -> bool:
    """Tell's us if there is symbols near the number."""
    pattern_symbol = re.compile('(' + '|'.join('! @ # \$ % \^ & \* \( \) \\ \| \/ } { \[ \] ! " № ; : \? - \+ = -'.split(' ')) + ')')
    search_result = re.search(pattern_symbol, sub_string)
    
    return bool(search_result)


def find_the_number(lines: list) -> int:
    """Finding all the parts numbers and create searching area for symbol.

    We find a number coordinates and search symbol around it to understand is this 'engine part' or not. If we find out
    that this number is engine part we breaks the cycle and go to next number.
    """
    result = 0
    pattern = re.compile('[0-9]+')
    
    # Find all coords of digits in line
    for index, line in enumerate(lines):
        coords_for_numbers = [(number.start(), number.end()) for number in re.finditer(pattern, line)]
        for start, end in coords_for_numbers:
            area_left = start - 1 if start else start
            area_right = end + 1 if end != len(line) else end
            area_top = index - 1 if index else index 
            area_bot = index + 1 if index != len(lines)-1 else index
            for i in range(area_top, area_bot+1):
                target_substr = lines[i][area_left:area_right]
                if is_number_valid(target_substr):
                    result += int(line[start:end])
                    break
    
    return result


def get_lines(filename: str) -> list:
    """Reading the input file."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

if __name__ == '__main__':
    lines = [line.strip() for line in get_lines('2023/03/input.txt')]
    engine_numbers = find_the_number(lines)
    print(engine_numbers)
