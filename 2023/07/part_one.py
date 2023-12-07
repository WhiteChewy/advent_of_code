"""Author: Nikita Kulikov (c) 07.12.2023

Advent Of Code. 1/2 puzzle.
"""
combinations = {
    'Five of a kind' : [],
    'Four of a kind' : [],
    'Full house' : [],
    'Three of a kind' : [],
    'Two pair' : [],
    'One pair' : [],
    'High card' : [],
}

def read_the_file(filename: str='2023/07/input.txt') -> list:
    '''Read the lines.'''
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def count_line_cards(line: str)->dict:
    types_of_cards = set(line)
    result_dict = {}
    for card in types_of_cards:
        result_dict[card] = line.count(card)
    return result_dict


def get_striped_lines(lines: list) -> list:
    result = []
    for line in lines:
        result.append(line.strip())
    return result

def dispence_lines_by_combinations(line: str) -> None:
    combination, bid = line.split(' ')
    dict_of_card_ins = count_line_cards(combination)
    if len(dict_of_card_ins) == 5:
        combinations['High card'].append(line)
    elif len(dict_of_card_ins) == 4:
        combinations['One pair'].append(line)
    elif len(dict_of_card_ins) == 1:
        combinations['Five of a kind'].append(line)
    else:
        d = {
            'four' : 0,
            'three' : 0,
            'two' : 0,
        }
        for card in dict_of_card_ins:
            if dict_of_card_ins[card] == 4:
                d['four'] += 1
            elif dict_of_card_ins[card] == 3:
                d['three'] += 1
            elif dict_of_card_ins[card] == 2:
                d['two'] += 1
        if d['four'] == 1:
            combinations['Four of a kind'].append(line)
        elif d['three'] == 1 and d['two'] == 1:
            combinations['Full house'].append(line)
        elif d['two'] == 2:
            combinations['Two pair'].append(line)
        else:
            combinations['Three of a kind'].append(line)

def compare(x: str):
    alphabet = 'A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2'.split(', ')
    d = {elem: num for num, elem in enumerate(alphabet)}
    if d[x] != ' ':
        return x

def get_ranks_inside_combinations(name: str, len_lines: int) -> int:
    alphabet = 'A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2'.split(', ')
    print(name)
    d = {elem: num for num, elem in enumerate(alphabet)}
    for elem in combinations[name].split(' '):
        if elem
        print(sorted(elem, key=compare))
    # for hand in zip(list(combinations[name])[0::],
    #                 list(combinations[name])[1::]):
    #     for char1, char2 in zip(hand[0], hand[1]):
    #         if d[char1] >= d [char2]:
    #             print(char1, char2)
    #     print(hand)
                

        


if __name__ == '__main__':
    lines = read_the_file('2023/07/test.txt')
    lines = get_striped_lines(lines)
    for line in lines:
        dispence_lines_by_combinations(line)
    for key in combinations:
        get_ranks_inside_combinations(key, len_lines=len(lines))
