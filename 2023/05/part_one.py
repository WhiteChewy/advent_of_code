"""Author: Nikita Kulikov (c) 05.12.2023

Advent Of Code second day. 1/2 puzzle.
"""
def get_seeds(lines: list) -> list:
    """Get seeds from almanac."""
    dirty_seeds = [int(seed) for seed in lines[0].strip().split(": ")[1].split(' ')]
    return dirty_seeds

def get_the_lines(filename: str='2023/05/input.txt') -> list:
    """Get file lines"""
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == '__main__':
    lines = get_the_lines('2023/05/test.txt')
    print(get_seeds(lines))

