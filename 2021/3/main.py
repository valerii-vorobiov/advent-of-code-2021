# Author = Valerii Vorobiov
# Date = 03 December, 2021
from collections import Counter, defaultdict


def part_one(_input):
    lines = _input.split()
    transposed = list(map(Counter, zip(*lines)))
    most_common_bits = [take_most_common_key(c) for c in transposed]
    gamma_rate = int(''.join(most_common_bits), 2)
    epsilon_rate = gamma_rate ^ int('1' * len(most_common_bits), 2)  # inverting bits
    return gamma_rate * epsilon_rate


def part_two(_input):
    lines = _input.split()
    return part_two_main(lines, pick_indices) * part_two_main(lines, lambda x: not pick_indices(x))


def take_most_common_key(c):
    return c.most_common(1)[0][0]


def pick_indices(d):
    return 1 if len(d[1]) >= len(d[0]) else 0


def part_two_main(lines, f):
    indices = list(range(len(lines)))
    for step in range(len(lines[0])):
        d = defaultdict(list)
        for l in indices:
            line = lines[l]
            d[int(line[step])].append(l)
        indices = d[f(d)]
        if len(indices) == 1:
            return int(lines[indices[0]], 2)


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), 'r') as input_file:
        return input_file.read()


_input = read_input()

print("Part One : " + str(part_one(_input)))

print("Part Two : " + str(part_two(_input)))
