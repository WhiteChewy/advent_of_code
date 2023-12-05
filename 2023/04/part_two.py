"""Author: Nikita Kulikov (c) 04.12.2023

Advent Of Code second day. 2/2 puzzle.
"""
import itertools


def calculate_winning_numbers(line: str, lines_number: int) -> int:
    """Count winning numbers."""
    number, tail = line.split(': ')
    number = int(number.split(' ')[-1])
    wining_numbers, ticket = tail.split(' | ')
    wining_numbers, ticket = wining_numbers.split(' '), ticket.split(' ')
    wining_numbers = [elem for elem in itertools.filterfalse(lambda x: not x, wining_numbers)]
    ticket = [elem for elem in itertools.filterfalse(lambda x: not x, ticket)]
    number_of_winning = 0
    for number in wining_numbers:
        if number in ticket:
                number_of_winning += 1

    return number_of_winning




def total_points(filename: str='2023/04/input.txt') -> int:
    """Count all points for file."""
    res1, res2, counts = 0, 0, []
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        m, o = [set(x.strip().split()) for x in line.split(':')[1].split('|')]
        win = len(m.intersection(o))
        count = 1 + (counts.pop(0) if counts else 0)
        if win:
            res1 += 2**(win-1)
            counts = [x+y for x, y in itertools.zip_longest(counts, [count]*win, fillvalue=0)]
        res2 += count
    
    return (res1, res2)
if __name__ == '__main__':
    print(total_points(), sep='\n')
