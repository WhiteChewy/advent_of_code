"""Author: Nikita Kulikov (c) 05.12.2023

Advent Of Code second day. 1/2 puzzle.
"""
import re
import datetime
from functools import reduce


def get_seeds(lines: list) -> list:
    """Get seeds from almanac."""
    dirty_seeds = [int(seed) for seed in lines[0].strip().split(": ")[1].split(' ')]
    return dirty_seeds


def get_map(lines: list) -> dict:
    """Get range of fields with names.

    {name: ranges}
    """
    all_text = reduce(lambda x, y: x+y, lines)
    pattern = r"\n(([a-zA-Z]+-)*[a-zA-Z]* map:)\n"
    names =[name for name, _ in re.findall(pattern, all_text)]
    dirty_groups = filter(lambda elem: elem[0].isdigit(), re.split(pattern, all_text)[1:])
    get_lists_in_dirty_groups = [elem.split('\n')[:-1] for elem in dirty_groups]
    groups = []
    for group in get_lists_in_dirty_groups:
        sub = []
        for subgroup in group:
            sub.append([int(elem) for elem in subgroup.split(' ')])
        groups.append(sub)
            
    map_of_almonac = {name: groups for name, groups in zip(names, groups)}
    return map_of_almonac

def get_the_lines(filename: str='2023/05/input.txt') -> list:
    """Get file lines"""
    with open(filename, 'r') as file:
        return file.readlines()

def seed_to_soil(seeds: list, seed_to_soil: list) -> int:
    '''Transform seeds to soil.'''
    result = []
    for seed in seeds:
        target = seed
        for ranges in seed_to_soil:
            soil_start = ranges[0]
            seed_start =ranges[1]
            range_length = ranges[2]
            if seed_start <= seed < seed_start+range_length:
                target = (soil_start-seed_start)-(-seed)
        result.append(target)

    return result

if __name__ == '__main__':
    lines = get_the_lines()
    seeds = get_seeds(lines)
    maps = get_map(lines)
    location = seeds
    for map in maps:
        location = seed_to_soil(location, maps[map])
    print(f'MIN: {min(location)}')
