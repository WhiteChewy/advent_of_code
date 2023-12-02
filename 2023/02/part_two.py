"""Author: Nikita Kulikov (c) 02.12.2023

Advent Of Code second day. 1/2 puzzle.
"""
import re
import functools

RED = 12
GREEN = 13
BLUE = 14

def total_number_of_color(line: str, colour: str) -> tuple:
    """Get max number of coubs with specific colours."""
    pattern = re.compile(f"([0-9]+ {colour})")
    search = pattern.findall(line)
    res = []
    for result in search:
        res.append(int(result.split()[0]))
    if res:
        return max(res)
    else:
        return 0


def is_game_possible(line: str) -> list:
    """Get power of cubes set."""
    game, rounds = re.split(': ', line)
    game_number = int(game.split(' ')[-1])
    result = 0
    blues = total_number_of_color(rounds, 'blue')
    reds = total_number_of_color(rounds, 'red')
    greens = total_number_of_color(rounds, 'green')
    return blues*reds*greens


def get_games(filename: str='2023/02_12_2023/input.txt') -> list:
    """Get games from file"""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines


if __name__ == '__main__':
    lines = get_games()
    powers = []
    for line in lines:
        flag = is_game_possible(line)
        powers.append(flag)
    print(functools.reduce(lambda x, y: x+y, powers))
