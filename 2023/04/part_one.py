"""Author: Nikita Kulikov (c) 04.12.2023

Advent Of Code second day. 1/2 puzzle.
"""
import itertools


def calculate_winning_numbers(line: str) -> int:
    """Count winning numbers."""
    _, tail = line.split(': ')
    wining_numbers, ticket = tail.split(' | ')
    wining_numbers, ticket = wining_numbers.split(' '), ticket.split(' ')
    wining_numbers = [elem for elem in itertools.filterfalse(lambda x: not x, wining_numbers)]
    ticket = [elem for elem in itertools.filterfalse(lambda x: not x, ticket)]
    pov = -1
    for number in wining_numbers:
        if number in ticket:
            pov += 1
    return 2**pov if pov != -1 else 0




def total_points(filename: str='04/input.txt') -> int:
    """Count all points for file."""
    res = 0
    with open(filename, 'r') as file:
        for line in file.readlines():
            res += calculate_winning_numbers(line.strip())
    
    return res

if __name__ == '__main__':
    print(total_points())
