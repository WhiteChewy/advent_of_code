"""Author: Nikita Kulikov (c) 02.12.2023

Advent Of Code second day. 1/2 puzzle.
"""
import re
import functools

RED = 12
GREEN = 13
BLUE = 14

def total_number_of_color(line: str, colour: str) -> tuple:
    """Get total number of coubs with specific colours."""
    pattern = re.compile(f"([0-9]+ {colour})")
    search = pattern.findall(line)
    res = 0
    for result in search:
        res += int(result.split()[0])

    return res
    


def is_game_possible(line: str) -> list:
    """Get number of cubes that where occured during the game."""
    rounds = re.split(': |; ', line)
    game_number = int(rounds[0].split(' ')[-1])
    result = 0
    for round in rounds:
        blues = total_number_of_color(round, 'blue')
        reds = total_number_of_color(round, 'red')
        greens = total_number_of_color(round, 'green')
        
        if reds > RED or blues > BLUE or greens > GREEN:
            result += 1
    if result == 0:
        return game_number
    else:
        return None
 
def get_games(filename: str='2023/02_12_2023/input.txt') -> list:
    """Get games from file"""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines


if __name__ == '__main__':
    lines = get_games()
    ids_possible = []
    for line in lines:
        flag = is_game_possible(line)
        if flag is not None:
            ids_possible.append(flag)
    print(functools.reduce(lambda x, y: x+y, ids_possible))
