# Author = Valerii Vorobiov
# Date = 08 December, 2021
from functools import partial


def part_one(_input):
    four_digits = [line.split(' | ')[1].split(' ') for line in _input.split('\n')]
    length = {
        1: 2,
        7: 3,
        4: 4,
        8: 7
    }
    return sum(1 for digits in four_digits for d in digits if len(d) in length.values())


def part_two(_input):
    four_digits = [line.split(' | ')[1].split(' ') for line in _input.split('\n')]
    ten_digits = [line.split(' | ')[0].split(' ') for line in _input.split('\n')]
    sums = []
    for i, digits_set in enumerate(ten_digits):
        mapping = get_mapping(digits_set)
        digits = apply_mapping(four_digits[i], mapping)
        sums.append(list_to_number(digits))
    return sum(sums)


def apply_mapping(digits, mapping):
    return [sorted([mapping[d] for d in digit]) for digit in digits]


def list_to_number(lists):
    numbers = [[1, 2, 3, 5, 6, 7],
               [3, 6],
               [1, 3, 4, 5, 7],
               [1, 3, 4, 6, 7],
               [2, 3, 4, 6],
               [1, 2, 4, 6, 7],
               [1, 2, 4, 5, 6, 7],
               [1, 3, 6],
               [1, 2, 3, 4, 5, 6, 7],
               [1, 2, 3, 4, 6, 7]]
    return int(''.join(str(numbers.index(l)) for l in lists))


def len_based(digits, lenth):
    return list(set(i) for i in digits if len(i) == lenth)


one = partial(len_based, lenth=2)
seven = partial(len_based, lenth=3)
four = partial(len_based, lenth=4)


def get_mapping(ten_digits):
    d = dict()
    d[1] = seven(ten_digits)[0] - one(ten_digits)[0]
    d[7] = (len_based(ten_digits, 5)[0].intersection(*len_based(ten_digits, 5)[1:]) - d[1]) - four(ten_digits)[0]
    d[4] = (len_based(ten_digits, 5)[0].intersection(*len_based(ten_digits, 5)[1:]) - d[1]) - d[7]
    d[2] = four(ten_digits)[0] - d[4] - one(ten_digits)[0]
    five = [i for i in len_based(ten_digits, 5) if len(i) > len(i - d[2])][0]
    d[6] = five - d[1] - d[7] - d[2] - d[4]
    d[3] = one(ten_digits)[0] - d[6]
    d[5] = set('abcdefg') - set(''.join(i) for i in d.values())
    return {''.join(v): k for k, v in d.items()}


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), 'r') as input_file:
        return input_file.read()


_input = read_input()

print("Part One : " + str(part_one(_input)))

print("Part Two : " + str(part_two(_input)))
