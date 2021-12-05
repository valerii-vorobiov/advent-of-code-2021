# Author = Valerii Vorobiov
# Date = 05 December, 2021
from collections import Counter


def part_one(_input):
    return main()


def part_two(_input):
    return main(True)


def parse_vector(line):
    start_c, end_c = line.split(' -> ')
    start_c = tuple(map(int, start_c.split(',')))
    end_c = tuple(map(int, end_c.split(',')))
    return Vector(start_c, end_c)


def main(diagonals=False):
    lines = _input.split('\n')
    d = Counter()
    vectors = [parse_vector(line) for line in lines]
    for vector in vectors:
        d.update(vector.generate_points_between(diagonals))
    return len([i for i in d.values() if i > 1])


class Vector:
    def __init__(self, start, end):
        self.start_x, self.start_y = start
        self.end_x, self.end_y = end

    def __repr__(self):
        return f'Vector(({self.start_x}, {self.start_y}), ({self.end_x}, {self.end_y}))'

    def generate_horisontal_points(self):
        return [(i, self.start_y) for i in range(min(self.start_x, self.end_x), max(self.start_x, self.end_x) + 1)]

    def generate_vertical_points(self):
        return [(self.start_x, i) for i in range(min(self.start_y, self.end_y), max(self.start_y, self.end_y) + 1)]

    def generate_diagonal_point(self, diff_x, diff_y):
        steps_x = list(range(min(0, diff_x), max(diff_x, 0) + 1))
        steps_y = list(range(min(0, diff_y), max(diff_y, 0) + 1))
        if diff_x < 0:
            steps_x.reverse()
        if diff_y < 0:
            steps_y.reverse()
        steps = zip(steps_x, steps_y)
        points = [(self.start_x + x, self.start_y + y) for x, y in steps]
        return points

    def generate_points_between(self, with_diagonal=False):
        if self.start_x == self.end_x:
            return self.generate_vertical_points()
        if self.start_y == self.end_y:
            return self.generate_horisontal_points()
        if with_diagonal:
            return self.generate_diagonal_point(self.end_x - self.start_x,
                                                self.end_y - self.start_y)
        return []


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), 'r') as input_file:
        return input_file.read()


_input = read_input()

print("Part One : " + str(part_one(_input)))

print("Part Two : " + str(part_two(_input)))
