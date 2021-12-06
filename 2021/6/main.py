# Author = Valerii Vorobiov
# Date = 06 December, 2021
from functools import lru_cache

import numpy as np


def part_one(_input):
    days = 80
    ages: np.array = np.array([int(age) for age in _input.split(',')])
    gen = np.array([-1] * len(ages))
    new_gen = []
    for day in range(days):
        for i in range(len(ages)):
            if ages[i] == 0:
                ages[i] = 7
                new_gen.append(8)
        ages = ages + gen
        ages = np.append(ages, new_gen)
        gen = np.append(gen, np.array([-1] * len(new_gen)))
        new_gen = []
    return ages.size


def part_two(_input):
    days = 18
    fishes = [int(age) for age in _input.split(',')]
    return sum(recurs(fish, days) for fish in fishes)


@lru_cache(maxsize=1000)
def recurs(life, days):
    if days < 1:
        return 1
    if life == 0:
        return recurs(6, days - 1) + recurs(8, days - 1)
    else:
        return recurs(0, days - life)


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), 'r') as input_file:
        return input_file.read()


_input = read_input()

print("Part One : " + str(part_one(_input)))

print("Part Two : " + str(part_two(_input)))
