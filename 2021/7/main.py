# Author = Valerii Vorobiov
# Date = 07 December, 2021
from math import ceil, floor
from statistics import mean, median


def part_one(_input):
    positions = sorted(list(map(int, _input.split(','))))
    return min(distance_one(positions, trend) for trend in trendlines(median, positions))


def part_two(_input):
    positions = sorted(list(map(int, _input.split(','))))
    return min(distance_two(positions, trend) for trend in trendlines(mean, positions))


def trendlines(f, l):
    return ceil(f(l)), floor(f(l))


def distance_one(l, trend_line):
    return sum(abs(i - trend_line) for i in l)


def distance_two(l, trend_line):
    return sum(sum_until(abs(i - trend_line)) for i in l)


def sum_until(n):
    return sum(range(1, n + 1))


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), 'r') as input_file:
        return input_file.read()


_input = read_input()

print("Part One : " + str(part_one(_input)))

print("Part Two : " + str(part_two(_input)))
